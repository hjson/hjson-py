hjson-py
========

`Hjson`_, the Human JSON. A configuration file format for humans.
Relaxed syntax, fewer mistakes, more comments.

Hjson works with Python 2.5+ and Python 3.3+ (based on `simplejson`_)

Installation
============

-  ``pip install hjson``

-  or download from https://pypi.python.org/pypi/hjson

Commandline
-----------

::

    Usage:
      hjson [options]
      hjson [options] <input>
      hjson (-h | --help)
      hjson (-V | --version)

    Options:
      -h --help     Show this screen.
      -j            Output as formatted JSON.
      -c            Output as JSON.
      -V --version  Show version.

E.g. ``echo '{"json":"obj"}' | hjson``


Usage
=====

.. code-block:: python

    import hjson

Decoding Hjson
--------------

.. code-block:: python

    text = """{
      foo: a
      bar: 1
    }"""

    hjson.loads(text)

Result:

.. code-block:: python

    OrderedDict([('foo', 'a'), ('bar', 1)])

Encoding Python object hierarchies
----------------------------------

.. code-block:: python

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

.. code-block:: python

    hjson.dumpsJSON(['foo', {'bar': ('baz', None, 1.0, 2)}])

Result: ``'["foo", {"bar": ["baz", null, 1.0, 2]}]'``

API
===

`hjson-py`_

.. _Hjson: http://hjson.org
.. _simplejson: https://github.com/simplejson/simplejson
.. _hjson-py: http://laktak.github.io/hjson-py/
