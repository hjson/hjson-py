#!/usr/bin/env python
from __future__ import with_statement

import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

IS_PYPY = hasattr(sys, 'pypy_translation_info')
VERSION = '1.0.0'
DESCRIPTION = "Simple, fast, extensible JSON encoder/decoder for Python"

with open('README.rst', 'r') as f:
   LONG_DESCRIPTION = f.read()

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
License :: OSI Approved :: Academic Free License (AFL)
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

if sys.platform == 'win32' and sys.version_info > (2, 6):
   # 2.6's distutils.msvc9compiler can raise an IOError when failing to
   # find the compiler
   # It can also raise ValueError http://bugs.python.org/issue7511
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError,
                 IOError, ValueError)
else:
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)

class BuildFailed(Exception):
    pass

class ve_build_ext(build_ext):
    # This class allows C extension building to fail.

    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError:
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except ext_errors:
            raise BuildFailed()


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        raise SystemExit(
            subprocess.call([sys.executable,
                             # Turn on deprecation warnings
                             '-Wd',
                             'hjson/tests/__init__.py']))

def run_setup():
    cmdclass = dict(test=TestCommand)
    kw = dict(cmdclass=cmdclass)

    setup(
        name="hjson",
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        classifiers=CLASSIFIERS,
        author="Christian Zangl",
        author_email="coralllama@gmail.com",
        url="http://github.com/laktak/hjson-py",
        license="MIT License",
        packages=['hjson', 'hjson.tests'],
        platforms=['any'],
        **kw)

run_setup()
