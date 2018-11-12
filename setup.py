from setuptools import setup
setup(
    name = 'BlockChainTx',
    version = '0.1.0',
    packages = ['BlockChainTx'],
    entry_points = {
        'console_scripts': [
            'BlockChainTx = BlockChainTx.__main__:main'
        ]
    })
