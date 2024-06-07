from setuptools import setup

setup(
    name='meu-cli',
    version='0.2',
    py_modules=['meu_cli'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        meu-cli=meu_cli:cli
    ''',
)
