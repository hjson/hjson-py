from unittest import TestCase

import hjson as json

class TestDefault(TestCase):
    def test_default(self):
        self.assertEqual(
            json.dumps(type, default=repr),
            json.dumps(repr(type)))
