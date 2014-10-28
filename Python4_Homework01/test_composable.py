#!/bin/env python
# -*- coding: utf-8 -*-

"""
test_composable.py performs simple tests of composable functions.
"""
import unittest
import string
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x*x

class ComposableTestCase(unittest.TestCase):
    
    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "a", "0123456789", string.ascii_lowercase :
            self.assertEqual(nulltran(s), s)
    
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * squarer
        for v, r in ((1,1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
    
    def test_power(self):
        squarer = Composable(square)
        po8 = squarer ** 3
        for v, r in ((1,1), (2, 256), (3, 6561)):
            self.assertEqual(po8(v), r)
    
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = square ** 0.5
        with self.assertRaises(TypeError):
            fc = square ** -2
        
if __name__ == "__main__":
    unittest.main()
