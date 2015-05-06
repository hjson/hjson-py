# hjson-py

[![Build Status](https://img.shields.io/travis/laktak/hjson-py.svg?style=flat-square)](http://travis-ci.org/laktak/hjson-py)
[![PyPI version](https://img.shields.io/pypi/v/hjson.svg?style=flat-square)](https://pypi.python.org/pypi/hjson)

[Hjson](http://hjson.org), the Human JSON. A data format that caters to humans and helps reduce the errors they make.

It supports `#`, `//` and `/**/` style comments as well as avoiding trailing/missing comma and other mistakes. For details and syntax see [hjson.org](http://hjson.org).

Hjson works with Python 2.5+ and Python 3.3+

The Python implementation of Hjson is based on [simplejson](https://github.com/simplejson/simplejson). For other platforms see [hjson.org](http://hjson.org).

# Installation

- `pip install hjson`

- or download from https://pypi.python.org/pypi/hjson

# Usage

```python
import hjson
```

## Decoding Hjson

```python
text = """{
  foo: a
  bar: 1
}"""

hjson.loads(text)
```

Result:
```python
OrderedDict([('foo', 'a'), ('bar', 1)])
```

## Encoding Python object hierarchies

```python
hjson.dumps({'foo': 'text', 'bar': (1, 2)})
```

Result:
```
{
  foo: text
  bar:
  [
    1
    2
  ]
}
```

## Encoding as JSON

Note that this is probably not as performant as the simplejson version.

```python
hjson.dumpsJSON(['foo', {'bar': ('baz', None, 1.0, 2)}])
```

Result:
`'["foo", {"bar": ["baz", null, 1.0, 2]}]'`


## From the Commandline

Use `hjson.tool` to validate and convert.

`python -m hjson.tool [FORMAT] [INFILE [OUTFILE]]`

Formats:

- `-h`: print Hjson
- `-j`: print formatted JSON
- `-c`: print compact JSON

E.g. `echo '{"json":"obj"}' | python -m hjson.tool`

# API

[hjson-py documentation](http://laktak.github.io/hjson-py/)

# Changes

- v1.5.0
  - Added support for optional root braces

- v1.4.1
  - Added documentation, links.

- v1.4.0
  - First release.
