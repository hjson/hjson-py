# hjson-py

[![Build Status](https://img.shields.io/travis/laktak/hjson-py.svg?style=flat-square)](http://travis-ci.org/laktak/hjson-py)
[![PyPI version](https://img.shields.io/pypi/v/hjson.svg?style=flat-square)](https://pypi.python.org/pypi/hjson)

Hjson, the Human JSON. A configuration file format that caters to humans and helps reduce the errors they make.

It supports `#`, `//` and `/**/` style comments as well as avoiding trailing/missing comma and other mistakes. For details and syntax see http://laktak.github.io/hjson.

Hjson works with Python 2.5+ and Python 3.3+ (forked from simplejson)

# BETA

**The parser is implemented and fully functional** (see `load`/`loads`).

The encoder currently outputs JSON but will return Hjson in a future update (see `dump`/`dumps`).

Please test and report bugs.

# Installation

- `pip install hjson`

- or download from https://pypi.python.org/pypi/hjson

# Usage

The parser supports the full Hjson syntax:

```
import hjson as hjson
obj = hjson.loads(hjsonText)
```

## From the Commandline

Use hjson.tool to validate and pretty-print:

`echo '{"json":"obj"}' | python -m hjson.tool`

# API

See the simplejson docs: http://simplejson.readthedocs.org/
