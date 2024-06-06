import base64
import binascii
import json
import os.path
import random
import secrets
import time
from dataclasses import dataclass, asdict
from enum import Enum
from hashlib import sha256
from typing import List, Optional, Union
from urllib import parse

import aiohttp
from playwright.async_api import Cookie, async_playwright


@dataclass
class _OIDCParams:
    client_id: str
    redirect_uri: str
    code_challenge: str
    code_challenge_method: str


@dataclass
class _OIDCBody:
    url: str
    nonce: str
    code_verifier: str
    params: _OIDCParams


@dataclass
class _Token:
    access_token: str
    refresh_token: str
    id_token: str


@dataclass
class _Translation:
    alternatives: List[str]
    text: str


class _BrowserType(Enum):
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'


def _random_hash() -> str:
    array_buffer = [secrets.randbits(32) for _ in range(28)]
    values = []
    for buffer in array_buffer:
        values.append(hex(buffer).replace('0x', '')[-2:])
    return ''.join(values)


def _create_code_challenge(text_to_encode: str):
    sha256_digest = sha256(text_to_encode.encode('utf-8')).digest()
    res = base64.b64encode(sha256_digest).decode()
    res = res.replace('=', '').replace('+', '-').replace('/', '_')
    return res


def _parse_session_type(token: _Token) -> str:
    data = token.access_token.split('.')[1].strip()
    try:
        body = base64.b64decode(data).decode('utf-8')
    except binascii.Error:
        body = base64.b64decode(data + '=').decode('utf-8')
    return json.loads(body)['sessionType']


def _encode_cookies(cookies: List[Cookie]) -> str:
    return '; '.join(f"{cookie['name']}={cookie['value']}" for cookie in cookies)


class _Deeplexer:

    _session_file: str

    _chrome_extension_app_id: str
    _chrome_extension_version: str
    _user_agent: str

    _session_type: Optional[str] = None
    _token: Optional[_Token] = None

    _username: Optional[str] = None
    _password: Optional[str] = None

    _browser_type: _BrowserType = _BrowserType.CHROMIUM
    _authorized: bool = False

    _client_id: str = 'chromeExtension'
    _code_challenge_method: str = 'S256'

    _json_rpc_user_agent_prefix: str = 'DeepLBrowserExtension'
    _json_rpc_free_url: str = 'https://www2.deepl.com/jsonrpc?client=chrome-extension'
    _json_rpc_pro_url: str = 'https://api.deepl.com/jsonrpc?client=chrome-extension'

    def __init__(self,
                 session_file: str,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 browser_type: Union[str, _BrowserType] = _BrowserType.CHROMIUM,
                 user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
                 chrome_extension_version: str = '1.12.3',
                 chrome_extension_app_id: str = 'cofdbpoegempjloogbagkncekinflcnj'):
        self._session_file = session_file
        self._username = username
        self._password = password

        if isinstance(browser_type, str):
            self._browser_type = _BrowserType[browser_type.upper()]
        else:
            self._browser_type = browser_type

        self._user_agent = user_agent
        self._chrome_extension_app_id = chrome_extension_app_id
        self._chrome_extension_version = chrome_extension_version

    async def __aenter__(self):
        await self.authorize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def _json_rpc_url(self) -> str:
        if self._session_type == 'Pro':
            return self._json_rpc_pro_url + ',' + self._chrome_extension_version
        else:
            return self._json_rpc_free_url + ',' + self._chrome_extension_version

    @property
    def chrome_extension_redirect_uri(self) -> str:
        return f'https://{self._chrome_extension_app_id}.chromiumapp.org/'

    @property
    def jsonrpc_user_agent(self) -> str:
        return f'{self._json_rpc_user_agent_prefix}/{self._chrome_extension_version} {self.user_agent}'

    @property
    def user_agent(self) -> str:
        return self._user_agent

    async def translate(
            self,
            text: Union[str, List[str]],
            source_lang: str,
            target_lang: str,
            proxy: Optional[str] = None) -> Union[_Translation, List[_Translation]]:
        if isinstance(text, str):
            translations = await self._translate_batch([text], source_lang, target_lang, proxy)
            assert len(translations) > 0, 'The translation has not returned proper results.'
            return translations[0]
        else:
            return await self._translate_batch(text, source_lang, target_lang, proxy)

    async def _translate_batch(
            self,
            texts: List[str],
            source_lang: str,
            target_lang: str,
            proxy: Optional[str] = None) -> List[_Translation]:
        async def _inner_translate_loop() -> Optional[List[_Translation]]:
            random.seed(time.time())
            num = random.randint(8300000, 8399998) * 1000

            async with aiohttp.ClientSession() as session:
                headers = {
                    'Content-Type': 'application/json; charset=utf-8',
                    'User-Agent': self.jsonrpc_user_agent,
                    'Accept': '*/*',
                    'Accept-Language': f'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Authorization': f'Bearer {self._token.access_token}',
                    'Origin': f'extension://{self._chrome_extension_app_id}',
                    'DNT': '1',
                    'Sec-GPC': '1',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.deepl.com/',
                    'Priority': 'u=4',
                }
                payload = {
                    'jsonrpc': '2.0',
                    'method': 'LMT_handle_texts',
                    'params': {
                        'texts': [{'text': text.replace('\n', '<br>')} for text in texts],
                        'html': 'enabled',
                        'lang': {
                            'target_lang': target_lang.upper(),
                            'source_lang_user_selected': source_lang.upper(),
                            'preference': {
                                'weight': {},
                            },
                        },
                        'commonJobParams': {},
                        'timestamp': round(time.time() * 1000),
                    },
                    'id': num,
                }
                async with session.post(self._json_rpc_url(), headers=headers, json=payload, proxy=proxy) as res:
                    if res.status != 200:
                        return None

                    body = await res.json()
            return [_Translation(
                alternatives=[alternative.replace('<br>', '\n') for alternative in result['alternatives']],
                text=result['text'].replace('<br>', '\n'),
            ) for result in body['result']['texts']]

        translations = await _inner_translate_loop()
        if not translations:
            self._token.access_token = await self._reauthorize()
            translations = await _inner_translate_loop()

        assert translations is not None, 'The translations must not be empty.'
        return translations

    async def authorize(self):
        if self._authorized:
            return

        if not self._username or not self._password:
            assert self._session_file is not None, (
                'Session file path must be provided if there are no username and password.'
            )

        if self._username and self._password and not os.path.exists(self._session_file):
            self._token = await self._authorize_session(self._username, self._password)
            with open(self._session_file, 'w') as f:
                json.dump(asdict(self._token), fp=f, ensure_ascii=False, indent=2)
        else:
            with open(self._session_file, 'r') as f:
                session = json.load(f)
            self._token = _Token(
                access_token=session['access_token'],
                refresh_token=session['refresh_token'],
                id_token=session['id_token'],
            )
            try:
                self._token.access_token = await self._reauthorize()
            except ValueError as e:
                if self._username and self._password:
                    self._token = await self._authorize_session(self._username, self._password)
                    with open(self._session_file, 'w') as f:
                        json.dump(asdict(self._token), fp=f, ensure_ascii=False, indent=2)
                else:
                    raise e

        self._session_type = _parse_session_type(self._token)
        self._authorized = True

    async def _reauthorize(self) -> str:
        async with aiohttp.ClientSession() as session:
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            payload = {
                'grant_type': 'refresh_token',
                'refresh_token': self._token.refresh_token,
            }
            async with session.post('https://w.deepl.com/oidc/token', headers=headers, data=payload) as res:
                if res.status != 200:
                    raise ValueError('Reauthorizing access token cannot be fulfilled. '
                                     'Sign in once again with your username and password.')

                body = await res.json()
        return body['access_token']

    async def _authorize_session(self, username: str, password: str) -> _Token:
        oidc_body = self._create_oidc_body()

        async def _create_cookies() -> List[Cookie]:
            async with async_playwright() as p:
                if self._browser_type == _BrowserType.CHROMIUM:
                    browser = await p.chromium.launch(headless=False)
                elif self._browser_type == _BrowserType.FIREFOX:
                    browser = await p.firefox.launch(headless=False)
                elif self._browser_type == _BrowserType.WEBKIT:
                    browser = await p.webkit.launch(headless=False)

                context = await browser.new_context()
                page = await context.new_page()
                await page.goto(oidc_body.url)
                await page.wait_for_timeout(250)

                element = await page.query_selector('input[name=email]')
                if element:
                    await element.click()
                    await page.keyboard.insert_text(username)
                    await page.keyboard.press('Tab', delay=250)
                    await page.keyboard.insert_text(password)
                    await page.wait_for_timeout(250)

                return await page.context.cookies()

        cookies = await _create_cookies()

        async def _signin() -> str:
            async with aiohttp.ClientSession() as session:
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Cookie': _encode_cookies(cookies),
                    'Origin': 'https://www.deepl.com',
                    'Priority': 'u=0, i',
                    'Referer': 'https://www.deep.com/',
                }
                payload = {
                    'username': username,
                    'password': password,
                    'redirect_uri': oidc_body.params.redirect_uri,
                    'client_id': oidc_body.params.client_id,
                    'code_challenge': oidc_body.params.code_challenge,
                    'code_challenge_method': oidc_body.params.code_challenge_method,
                    'state': 'undefined',
                    'nonce': oidc_body.nonce,
                }
                async with session.post('https://w.deepl.com/oidc/login',
                                        headers=headers,
                                        data=payload,
                                        allow_redirects=False) as res:
                    if res.status != 302 and res.status != 301:
                        raise ValueError(f'DeepL sign in service returned status code: {res.status} {res.reason}')

                    location = res.headers['Location']
            params = location.split('?')[1]
            params = parse.parse_qs(params, keep_blank_values=True)
            return params['code'][0]

        try:
            code = await _signin()
        except aiohttp.ClientError as e:
            raise ValueError('Failed to sign in DeepL:', e)

        async def _authorize() -> _Token:
            async with aiohttp.ClientSession() as session:
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
                payload = {
                    'client_id': oidc_body.params.client_id,
                    'code_verifier': oidc_body.code_verifier,
                    'code': code,
                    'grant_type': 'authorization_code',
                    'redirect_uri': self.chrome_extension_redirect_uri,
                }
                async with session.post('https://w.deepl.com/oidc/token', headers=headers, data=payload) as res:
                    body = await res.json()
            return _Token(access_token=body['access_token'],
                          refresh_token=body['refresh_token'],
                          id_token=body['id_token'])

        return await _authorize()

    def _create_oidc_body(self) -> _OIDCBody:
        nonce = _random_hash()
        code_verifier = _random_hash()
        code_challenge = _create_code_challenge(code_verifier)

        params = {
            'client_id': [self._client_id],
            'redirect_uri': [self.chrome_extension_redirect_uri],
            'code_challenge': [code_challenge],
            'code_challenge_method': [self._code_challenge_method],
            'nonce': [nonce],
        }
        url_encoded_params = parse.urlencode(params, doseq=True)
        return _OIDCBody(
            url='https://www.deepl.com/ko/login?' + url_encoded_params,
            nonce=nonce,
            code_verifier=code_verifier,
            params=_OIDCParams(
                client_id=self._client_id,
                redirect_uri=self.chrome_extension_redirect_uri,
                code_challenge=code_challenge,
                code_challenge_method=self._code_challenge_method,
            )
        )

