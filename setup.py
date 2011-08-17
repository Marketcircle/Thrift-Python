#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

try:
    from setuptools import setup, Extension
except:
    from distutils.core import setup, Extension

fastbinarymod = Extension('thrift.protocol.fastbinary',
                    sources = ['src/protocol/fastbinary.c'],
                )

setup(name = 'thrift',
    version = '0.8.0-dev',
    description = 'Python bindings for the Apache Thrift RPC system',
    author = ['Thrift Developers'],
    author_email = ['dev@thrift.apache.org'],
    url = 'http://thrift.apache.org',
    license = 'Apache License 2.0',
    packages = [
        'thrift',
        'thrift.protocol',
        'thrift.transport',
        'thrift.server',
    ],
    package_dir = {'thrift' : 'src'},
    ext_modules = [fastbinarymod],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Networking'
    ]
)

