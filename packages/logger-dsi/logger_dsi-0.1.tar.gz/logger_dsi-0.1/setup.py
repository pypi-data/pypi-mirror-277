# setup.py

from setuptools import setup, find_packages

setup(
    name="logger_dsi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Design Systems Inno.",
    author_email="sebastian@dsinno.io",
    description="A Python client library to send logs to Loki.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://bitbucket.org/dsinno/lokiclient",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
