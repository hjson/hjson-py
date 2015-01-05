# hjson-py

[![Build Status](https://img.shields.io/travis/laktak/hjson-py.svg?style=flat-square)](http://travis-ci.org/laktak/hjson-py)

Hjson, the Human JSON. A data format that caters to humans and helps reduce the errors they make.

It supports `#`, `//` and `/**/` style comments as well as avoiding trailing/missing comma and other mistakes. For details and syntax see http://laktak.github.io/hjson.

hjson-py should work on Python 2.5+ and Python 3.3+ (forked from from simplejson)

# BETA

Please test and report bugs.

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
