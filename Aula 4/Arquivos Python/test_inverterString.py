import unittest
from inverterString import inverterString

class test_inverterString(unittest.TestCase):
    def test_palavra(self):
        self.assertEqual(inverterString("Python"), "nohtyP")

    def test_vazia(self):
        self.assertEqual(inverterString(""), "")

    def test_espacos(self):
        self.assertEqual(inverterString("a b"), "b a")