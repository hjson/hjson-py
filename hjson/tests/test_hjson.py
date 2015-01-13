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

    def load(self, name, cr):
        name = os.path.join(self.assetsDir, name)
        with open(name, 'rb') as f:
            text = f.read().replace('\r', '')
            if cr: text = text.replace('\n', '\r\n')
            return text

    def check(self, name, file, isJson, inputCr):
        text = self.load(file, inputCr)
        shouldFail = name[0:4] == "fail"

        try:
            data = json.loads(text)
            text1 = json.dumps(data, sort_keys=True)
            self.assertFalse(shouldFail)

            result = json.loads(self.load(name + "_result.json", inputCr))
            text2 = json.dumps(result, sort_keys=True)
            self.assertEqual(text2, text1)

            # todo name + "_result.hjson"

        except json.JSONDecodeError as e:
            self.assertTrue(shouldFail)

    def test_files(self):
        for file in self.assets:
            name, sep, ext = file.partition("_test.")
            if not sep: continue

            isJson = ext == "json"
            self.check(name, file, isJson, True)
            self.check(name, file, isJson, False)
