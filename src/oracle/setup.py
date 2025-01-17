#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

VERSION = "1.0.0"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'cryptography'
]

setup(
    name='oracle',
    version=VERSION,
    description='oracle assessment tester',
    long_description='oracle assessment tester',
    license='MIT',
    author='Microsoft Corporation',
    author_email='vmanhas@microsoft.com',
    url='https://github.com/Azure/azure-cli-extensions/tree/main/src/oracleassess',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_oracle': ['azext_metadata.json']}
)