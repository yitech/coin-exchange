from setuptools import setup, find_packages

setup(
    name='exhost',
    version='1.0',
    description='client of grpc for user send order',
    author='Yi Te',
    author_email='coastq22889@icloud.com',
    packages=find_packages(),
    install_requires=[
        'git+https://github.com/yitech/coin-infra.git',
    ],
)