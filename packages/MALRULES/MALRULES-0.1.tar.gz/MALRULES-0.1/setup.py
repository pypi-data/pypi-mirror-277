# setup.py

from setuptools import setup, find_packages

setup(
    name='MALRULES',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'MALHasher',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    author='Joy Mondal',
    author_email='Contact.Joymondal@gmail.com',
    description='MALRULES is a Python package for heuristic malware analysis and file hashing. It provides functionalities to analyze files for potential malware by checking for suspicious patterns, API calls, and strings. The package also includes utilities for generating SHA256 and SHA1 file hashes using the MALHasher library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/codewithjoymondal',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
