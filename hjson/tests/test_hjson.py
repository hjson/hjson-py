from __future__ import with_statement

import os
import sys
import subprocess
import tempfile

from unittest import TestCase

import hjson as json

class TestIndent(TestCase):

    assetsDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
    assets = os.listdir(assetsDir)
    maxDiff = None

    def get(self, name):
        name = os.path.join(self.assetsDir, name)
        with open(name, 'rb') as f:
            return f.read()

    def test_files(self):
        for file in self.assets:
            name, sep, ext = file.partition("_test.")
            if not sep: continue

            isJson = ext == "json"

            text = self.get(file)
            shouldFail = name[0:4] == "fail"

            try:
                data = json.loads(text)
                text1 = json.dumps(data)
                self.assertFalse(shouldFail)

                result = json.loads(self.get(name + "_result.json"))
                text2 = json.dumps(result)
                self.assertEqual(text2, text1)

                # todo name + "_result.hjson"

            except json.JSONDecodeError as e:
                self.assertTrue(shouldFail)

