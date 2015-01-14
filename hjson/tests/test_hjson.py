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
    verma, vermi = sys.version_info[0:2]

    def load(self, name, cr):
        name = os.path.join(self.assetsDir, name)
        with open(name, 'rb') as f:
            text = f.read().decode('utf-8')
            text = text.replace('\r', '')
            if cr: text = text.replace('\n', '\r\n')
            return text

    def check(self, name, file, inputCr):
        text = self.load(file, inputCr)
        shouldFail = name[0:4] == "fail"

        try:
            data = hjson.loads(text)
            self.assertFalse(shouldFail)

            text1 = hjson.dumpsJSON(data)
            hjson1 = hjson.dumps(data, ensure_ascii=False);
            result = hjson.loads(self.load(name + "_result.json", inputCr))
            text2 = hjson.dumpsJSON(result)
            hjson2 = self.load(name + "_result.hjson", False)

            if self.verma>2 or self.vermi>6:
                # final check fails on py2.6 because of string formatting issues
                self.assertEqual(text2, text1)
                self.assertEqual(hjson2, hjson1)

            # dbg
            # with open(name + "_dbg1.txt", "w") as tmp: tmp.write(hjson1.encode("utf-8"))
            # with open(name + "_dbg2.txt", "w") as tmp: tmp.write(hjson2.encode("utf-8"))


        except hjson.HjsonDecodeError as e:
            self.assertTrue(shouldFail)

    def test_files(self):
        for file in self.assets:
            name, sep, ext = file.partition("_test.")
            if not sep: continue

            self.check(name, file, True)
            self.check(name, file, False)
