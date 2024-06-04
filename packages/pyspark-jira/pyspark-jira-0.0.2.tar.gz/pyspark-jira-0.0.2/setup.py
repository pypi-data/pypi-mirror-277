#!/usr/bin/env python
from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


dist = setup(
    name='pyspark-jira',
    version="0.0.2",
    description='PySpark JIRA Data Source',
    author='Hyukjin Kwon',
    author_email='gurwls223@apache.org',
    url='https://github.com/HyukjinKwon/pyspark-jira',
    license='Apache License 2.0',
    packages=['pyspark_jira'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    test_suite='tests',
    python_requires='>=3.10',
)
