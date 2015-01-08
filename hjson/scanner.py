"""JSON token scanner
"""
import re

__all__ = ['make_scanner', 'JSONDecodeError']

class JSONDecodeError(ValueError):
    """Subclass of ValueError with the following additional properties:

    msg: The unformatted error message
    doc: The JSON document being parsed
    pos: The start index of doc where parsing failed
    end: The end index of doc where parsing failed (may be None)
    lineno: The line corresponding to pos
    colno: The column corresponding to pos
    endlineno: The line corresponding to end (may be None)
    endcolno: The column corresponding to end (may be None)

    """
    # Note that this exception is used from _speedups
    def __init__(self, msg, doc, pos, end=None):
        ValueError.__init__(self, errmsg(msg, doc, pos, end=end))
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.end = end
        self.lineno, self.colno = linecol(doc, pos)
        if end is not None:
            self.endlineno, self.endcolno = linecol(doc, end)
        else:
            self.endlineno, self.endcolno = None, None

    def __reduce__(self):
        return self.__class__, (self.msg, self.doc, self.pos, self.end)


def linecol(doc, pos):
    lineno = doc.count('\n', 0, pos) + 1
    if lineno == 1:
        colno = pos + 1
    else:
        colno = pos - doc.rindex('\n', 0, pos)
    return lineno, colno


def errmsg(msg, doc, pos, end=None):
    lineno, colno = linecol(doc, pos)
    msg = msg.replace('%r', repr(doc[pos:pos + 1]))
    if end is None:
        fmt = '%s: line %d column %d (char %d)'
        return fmt % (msg, lineno, colno, pos)
    endlineno, endcolno = linecol(doc, end)
    fmt = '%s: line %d column %d - line %d column %d (char %d - %d)'
    return fmt % (msg, lineno, colno, endlineno, endcolno, pos, end)


def make_scanner(context):
    parse_object = context.parse_object
    parse_array = context.parse_array
    parse_string = context.parse_string
    parse_mlstring = context.parse_mlstring
    parse_tfnns = context.parse_tfnns
    encoding = context.encoding
    strict = context.strict
    object_hook = context.object_hook
    object_pairs_hook = context.object_pairs_hook
    memo = context.memo

    def _scan_once(string, idx):
        try:
            ch = string[idx]
        except IndexError:
            raise JSONDecodeError('Expecting value', string, idx)

        if ch == '"':
            return parse_string(string, idx + 1, encoding, strict)
        elif ch == '{':
            return parse_object((string, idx + 1), encoding, strict,
                _scan_once, object_hook, object_pairs_hook, memo)
        elif ch == '[':
            return parse_array((string, idx + 1), _scan_once)
        elif ch == '\'' and string[idx:idx + 3] == '\'\'\'':
            return parse_mlstring(string, idx)

        return parse_tfnns(context, string, idx)

    def scan_once(string, idx):
        if idx < 0:
            # Ensure the same behavior as the C speedup, otherwise
            # this would work for *some* negative string indices due
            # to the behavior of __getitem__ for strings. #98
            raise JSONDecodeError('Expecting value', string, idx)
        try:
            return _scan_once(string, idx)
        finally:
            memo.clear()

    return scan_once
