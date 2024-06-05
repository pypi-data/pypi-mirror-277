# setup.py
from setuptools import setup, find_packages

setup(
    name="dfrint",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    author="",
    author_email="",
    description="A package with delay_print, delay_input and fast_print",
    url="https://github.com/Devdeczin/dfrint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
