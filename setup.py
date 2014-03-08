#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()

setup(
    name='wakeonlan',
    version='0.2.0',
    description='A small python module for wake on lan.',
    url='https://github.com/remcohaszing/pywakeonlan',
    author='Remco Haszing',
    author_email='remcohaszing@gmail.com',
    packages=['wakeonlan'],
    license='WTFPL',
    long_description=readme,
    scripts=['script/wol'])