#!/usr/bin/python3
"""
setup mysql client
"""

from setuptools import setup, Extension

setup(
    name='MyMySQLClient',
    version='1.0',
    author='Yohanes Senbeto',
    author_email='jonicasenbeto@email.com',
    description='A MySQL client package',
    long_description='A Python package for interacting with MySQL databases.',
    url='https://github.com/YohanesSenbeto/mymysqlclient',  # Replace with your GitHub repository URL
    packages=['mymysqlclient'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'other_dependency',
        # Add any other dependencies required by your package
    ],
)

