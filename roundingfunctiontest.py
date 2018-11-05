import unittest
from roundingfunction import roundFunction

class RoundingTestCase(unittest.TestCase):

    def test_int_round_down(self):
        answer = roundFunction(249.45, 0)
        self.assertEqual(answer, 249)

    def test_int_round_up(self):
        answer = roundFunction(249.85, 0)
        self.assertEqual(answer, 250)

    def test_decimal_round_up(self): # Dangit, it's no use. My rounding function is no better than python's default one...
        answer = roundFunction(249.45, 1) # floats....
        self.assertEqual(answer, 249.5)

    def test_decimal_round_down(self):
        answer = roundFunction(249.814, 2)
        self.assertEqual(answer, 249.81)

    def test_multi_9_decimal(self):
        answer = roundFunction(1238.33999, 4)
        self.assertEqual(answer, 1238.34)

    def test_multi_9_decimal_carryover(self):
        answer = roundFunction(1249.99999, 1)
        self.assertEqual(answer, 1250)

    def test_negdecimalPlace_down(self):
        answer = roundFunction(174, -1)
        self.assertEqual(answer, 170)

    def test_negdecimalPlace_up(self):
        answer = roundFunction(177.925, -2)
        self.assertEqual(answer, 200)

    def test_negdecimalPlace_invalidDecimal(self):
        answer = roundFunction(15, -2)
        self.assertEqual(answer, 'Error: decimalPlace out of bounds')

unittest.main()