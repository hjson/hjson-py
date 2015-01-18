hjson-py
========

`Hjson`_, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports ``#``, ``//`` and ``/**/`` style comments as well as
avoiding trailing/missing comma and other mistakes. For details and
syntax see `hjson.org`_.

Hjson works with Python 2.5+ and Python 3.3+ (based on `simplejson`_)

Installation
============

-  ``pip install hjson``

-  or download from https://pypi.python.org/pypi/hjson

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

From the Commandline
--------------------

Use ``hjson.tool`` to validate and convert.

``python -m hjson.tool [FORMAT] [INFILE [OUTFILE]]``

Formats:

-  ``-h``: print Hjson
-  ``-j``: print formatted JSON
-  ``-c``: print compact JSON

E.g. ``echo '{"json":"obj"}' | python -m hjson.tool``

API
===

`hjson-py`_

.. _Hjson: http://hjson.org
.. _hjson.org: http://hjson.org
.. _simplejson: https://github.com/simplejson/simplejson
.. _hjson-py: http://laktak.github.io/hjson-py/
