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
        with open(name, 'rb') as f:
            return f.read()

    def test_files(self):
        for file in self.assets:
            if file[-11:] != "_test.hjson": continue

            file = os.path.join(self.assetsDir, file)
            name = file[:-11]

            source = self.get(file)
            res = json.loads(self.get(name + "_result.json"))

            textfile = name + "_result.txt"
            # if os.path.exists(textfile):
            # todo: dump is not yet supported

            try:
                obj = json.loads(source)
                text = json.dumps(obj)
                self.assertEqual(json.dumps(res["data"]), text)
            except json.JSONDecodeError as e:
                # error messages differ, just check if it should throw
                self.assertTrue(res["err"])

