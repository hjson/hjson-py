from __future__ import with_statement

import os
import sys
import subprocess
import tempfile

from unittest import TestCase

import hjson

class TestAssets(TestCase):

    assetsDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
    assets = os.listdir(assetsDir)
    maxDiff = None

    def load(self, name, cr):
        name = os.path.join(self.assetsDir, name)
        with open(name, 'rb') as f:
            text = f.read().replace('\r', '')
            if cr: text = text.replace('\n', '\r\n')
            return text

    def check(self, name, file, inputCr):
        text = self.load(file, inputCr)
        shouldFail = name[0:4] == "fail"

        try:
            data = hjson.loads(text)
            self.assertFalse(shouldFail)

            text1 = hjson.dumpsJSON(data)
            hjson1 = hjson.dumps(data);
            result = hjson.loads(self.load(name + "_result.json", inputCr))
            text2 = hjson.dumpsJSON(result)
            hjson2 = self.load(name + "_result.hjson", False)

            #todo
            #self.assertEqual(text2, text1)
            #self.assertEqual(hjson2, hjson1)

        except hjson.HjsonDecodeError as e:
            self.assertTrue(shouldFail)

    def test_files(self):
        for file in self.assets:
            name, sep, ext = file.partition("_test.")
            if not sep: continue

            self.check(name, file, True)
            self.check(name, file, False)
