# test_module1

from Add2num import add2num

import unittest


def setUpModule():
    print("Executed before an test in the module")


def tearDownModule():
    print("Executed after an test in the module")


class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
        self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_1neg_num(self):
        self.assertEqual(add2num(-10, 9), -1)


if __name__ == '__main__':
    unittest.main()
