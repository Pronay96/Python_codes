# test_module2

from proj.Add2num import add2num

import unittest

class SampleTestClass(unittest.TestCase):

    def test_sample(self):
        self.assertRaises(TypeError, add2num, 3, 'hello')
