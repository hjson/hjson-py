hjson-py
========

Hjson, the Human JSON. A configuration file format that caters to humans
and helps reduce the errors they make.

It supports ``#``, ``//`` and ``/**/`` style comments as well as
avoiding trailing/missing comma and other mistakes. For details and
syntax see http://laktak.github.io/hjson.

Hjson works with Python 2.5+ and Python 3.3+ (forked from simplejson)

Installation
============

-  ``pip install hjson``

-  or download from https://pypi.python.org/pypi/hjson

Usage
=====

::

    import hjson

Decoding Hjson
--------------

::

    text = """{
      foo: a
      bar: 1
    }"""

    hjson.loads(text)

Result:

::

    OrderedDict([('foo', 'a'), ('bar', 1)])

Encoding Python object hierarchies
----------------------------------

::

    hjson.dumps({'foo': 'text', 'bar': (1, 2)})

Result:

::

    {
      foo: text
      bar:
      [
        1
        2
      ]
    }

Encoding as JSON
----------------

Note that this is probably not as performant as the simplejson version.

::

    hjson.dumpsJSON(['foo', {'bar': ('baz', None, 1.0, 2)}])

Result: ``'["foo", {"bar": ["baz", null, 1.0, 2]}]'``

From the Commandline
--------------------

Use hjson.tool to validate and convert.

``python -m hjson.tool [FORMAT] [INFILE [OUTFILE]]``

Formats: - ``-h``: print Hjson - ``-j``: print formatted JSON - ``-c``:
print compact JSON

E.g. ``echo '{"json":"obj"}' | python -m hjson.tool``

API
===

See the simplejson docs: http://simplejson.readthedocs.org/
