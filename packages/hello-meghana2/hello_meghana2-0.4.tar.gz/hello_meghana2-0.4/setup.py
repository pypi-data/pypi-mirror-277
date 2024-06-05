# setup.py
from setuptools import setup, find_packages

setup(
    name='hello_meghana2',
    version='0.4',
    description='A simple World package',
    author='megha',
    author_email='meghanabl2112@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'hello-meghana=hello_meghana.cli:greet',
        ],
    },
)
