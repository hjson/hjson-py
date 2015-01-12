#!/usr/bin/env python
from __future__ import with_statement

import sys
try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

IS_PYPY = hasattr(sys, 'pypy_translation_info')
VERSION = '1.3.0'
DESCRIPTION = "JSON for Humans, allows comments and is less error prone."

with open('README.rst', 'r') as f:
   LONG_DESCRIPTION = f.read()

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 4 - Beta
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

class BuildFailed(Exception):
    pass

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
        keywords="json comments configuration",
        classifiers=CLASSIFIERS,
        author="Christian Zangl",
        author_email="coralllama@gmail.com",
        url="http://github.com/laktak/hjson-py",
        license="MIT License",
        packages=['hjson', 'hjson.tests'],
        platforms=['any'],
        **kw)

run_setup()
