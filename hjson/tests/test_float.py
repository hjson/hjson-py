import math
from unittest import TestCase
from hjson.compat import long_type, text_type
import hjson as json
from hjson.decoder import NaN, PosInf, NegInf

class TestFloat(TestCase):

    def test_degenerates_ignore(self):
        for f in (PosInf, NegInf, NaN):
            self.assertEqual(json.loads(json.dumps(f)), None)

    def test_floats(self):
        for num in [1617161771.7650001, math.pi, math.pi**100,
                    math.pi**-100, 3.1]:
            self.assertEqual(float(json.dumps(num)), num)
            self.assertEqual(json.loads(json.dumps(num)), num)
            self.assertEqual(json.loads(text_type(json.dumps(num))), num)

    def test_ints(self):
        for num in [1, long_type(1), 1<<32, 1<<64]:
            self.assertEqual(json.dumps(num), str(num))
            self.assertEqual(int(json.dumps(num)), num)
            self.assertEqual(json.loads(json.dumps(num)), num)
            self.assertEqual(json.loads(text_type(json.dumps(num))), num)
