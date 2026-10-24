from unittest import TestCase

import hjson as json


class TestBigintAsString(TestCase):
    # Python 2.5, at least the one that ships on Mac OS X, calculates
    # 2 ** 53 as 0! It manages to calculate 1 << 53 correctly.
    values = [(200, 200),
              ((1 << 53) - 1, 9007199254740991),
              ((1 << 53), '9007199254740992'),
              ((1 << 53) + 1, '9007199254740993'),
              (-100, -100),
              ((-1 << 53), '-9007199254740992'),
              ((-1 << 53) - 1, '-9007199254740993'),
              ((-1 << 53) + 1, -9007199254740991)]

    options = (
        {"bigint_as_string": True},
        {"int_as_string_bitcount": 53}
    )

    def test_ints(self):
        for opts in self.options:
            for val, expect in self.values:
                self.assertEqual(
                    val,
                    json.loads(json.dumpsJSON(val)))
                self.assertEqual(
                    expect,
                    json.loads(json.dumpsJSON(val, **opts)))

    def test_lists(self):
        for opts in self.options:
            for val, expect in self.values:
                val = [val, val]
                expect = [expect, expect]
                self.assertEqual(
                    val,
                    json.loads(json.dumpsJSON(val)))
                self.assertEqual(
                    expect,
                    json.loads(json.dumpsJSON(val, **opts)))

    def test_dicts(self):
        for opts in self.options:
            for val, expect in self.values:
                val = {'k': val}
                expect = {'k': expect}
                self.assertEqual(
                    val,
                    json.loads(json.dumpsJSON(val)))
                self.assertEqual(
                    expect,
                    json.loads(json.dumpsJSON(val, **opts)))

    def test_dict_keys(self):
        for opts in self.options:
            for val, _ in self.values:
                expect = {str(val): 'value'}
                val = {val: 'value'}
                self.assertEqual(
                    expect,
                    json.loads(json.dumpsJSON(val)))
                self.assertEqual(
                    expect,
                    json.loads(json.dumpsJSON(val, **opts)))


class TestHjsonBigInt(TestCase):
    def test_hjson_integer_string_options(self):
        for options, bits in (({'bigint_as_string': True}, 53),
                              ({'int_as_string_bitcount': 8}, 8)):
            for value in (-(1 << bits) - 1, -(1 << bits),
                          (1 << bits), (1 << bits) + 1):
                for wrap in (lambda x: x, lambda x: [x], lambda x: {'value': x}):
                    encoded = json.dumps(wrap(value), **options)
                    self.assertEqual(json.loads(encoded), wrap(str(value)))

    def test_hjson_small_integers_and_default_stay_numeric(self):
        for bits in (8, 53):
            for value in (-(1 << bits) + 1, -1, 0, 1, (1 << bits) - 1):
                self.assertEqual(json.loads(json.dumps(
                    value, int_as_string_bitcount=bits)), value)
        value = 1 << 60
        self.assertEqual(json.loads(json.dumps(value)), value)

    def test_bigint_option_takes_precedence_over_bitcount(self):
        value = 1 << 8
        self.assertEqual(json.loads(json.dumps(
            value, bigint_as_string=True, int_as_string_bitcount=8)), value)

    def test_hjson_dump_and_noninteger_values(self):
        from io import StringIO
        value = 1 << 53
        stream = StringIO()
        json.dump({value: [value, True, False, None, 1.5]}, stream,
                  bigint_as_string=True)
        self.assertEqual(json.loads(stream.getvalue()),
                         {str(value): [str(value), True, False, None, 1.5]})
