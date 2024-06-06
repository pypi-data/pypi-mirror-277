# DeepLexer

Working DeepL Pro even Quota Exceeded.

Use your own risks.

## Usage
```
pip install deeplexer
```

```python
import asyncio
from deeplexer import Deeplexer

async def main():
    session_file = './sessions.json'  # Required. Path to the session be stored.
    username = '<deepl username>'  # Optional if session file is valid
    password = '<deepl password>'  # Optional if session file is valid
    async with Deeplexer(session_file, 
                         username=username, 
                         password=password) as deeplex:
        query = 'Hello World!'
        translation = await deeplex.translate(query, 'EN', 'KO')
        print('Translation:', translation.text)
    print('All jobs have been finished')

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()
```

## License

Licensed under the [MIT license](https://github.com/OrigamiDream/deeplexer/blob/main/LICENSE).
