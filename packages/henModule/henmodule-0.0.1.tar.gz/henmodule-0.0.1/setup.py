from setuptools import setup, find_packages

setup(
    name='henModule',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='carlos vassoler',
    author_email='carloshtvassoler@gmail.com',
    description='free and open source module to perform heat integration designs',
    url='https://github.com/CarlosTadeuVassoler/hen-module',
    python_requires='>=3.6',
)