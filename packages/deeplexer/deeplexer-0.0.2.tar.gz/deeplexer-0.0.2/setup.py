from setuptools import setup, find_packages

setup(
    name='deeplexer',
    version='0.0.2',
    description='Free DeepL Pro even Quota Exceeded',
    url='https://github.com/OrigamiDream/deeplexer.git',
    author='OrigamiDream',
    author_email='hello@origamidream.me',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(exclude=[]),
    platforms='any',
    install_requires=[
        'aiohttp>=3.9.5',
        'brotli>=1.1.0',
        'playwright>=1.44.0',
    ],
    python_requires='>=3.10',
    keywords=[
        'machine translation',
        'translate',
        'translation',
        'deepl',
        'deeplx',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
