# test_module3

from proj.Add2num import add2num

import unittest

class SampleTestClass(unittest.TestCase):

    @unittest.expectedFailure
    def test_sample(self):
        with self.assertRaises(ValueError) as e:
            r = add2num(3, 'hello')
        self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")
