r"""Command-line tool to validate and pretty-print JSON

Usage::

    $ echo '{"json":"obj"}' | python -m hjson.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m hjson.tool
    Expecting property name: line 1 column 2 (char 2)

"""
from __future__ import with_statement
import sys
import hjson

def main():
    todo = "-h"
    args = []
    for arg in sys.argv[1:]:
        if arg[0] == '-':
            todo = arg
        else:
            args.append(arg)

    if len(args) == 0:
        infile = sys.stdin
        outfile = sys.stdout
    elif len(args) == 1:
        infile = open(args[0], 'r')
        outfile = sys.stdout
    elif len(args) == 2:
        infile = open(args[0], 'r')
        outfile = open(args[1], 'w')
    else:
        raise SystemExit(sys.argv[0] + " {-h|-j|-c} [infile [outfile]]")

    with infile:
        try:
            obj = hjson.load(infile, use_decimal=True)
        except ValueError:
            raise SystemExit(sys.exc_info()[1])

    with outfile:
        if todo == '-j':
            hjson.dumpJSON(obj, outfile, use_decimal=True, indent="  ")
        elif todo == '-c':
            hjson.dumpJSON(obj, outfile, use_decimal=True, separators=(',', ':'))
        else:
            hjson.dump(obj, outfile, use_decimal=True)

        outfile.write('\n')

if __name__ == '__main__':
    main()
