# test_module2

from Pow2num import pow2num

import unittest

class Testpow2num(unittest.TestCase):

    def setUp(self):
        print("Executed before start of every test")

    def tearDown(self):
        print("Excluded at the end of every test")

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)


if __name__ == '__main__':
    unittest.main()