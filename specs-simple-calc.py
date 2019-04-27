from simple_calc import SimpleCalc

import unittest

class Calc_tests(unittest.TestCase):
    #Initiating a calculator object so we can test its behaviour
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6, "You failed to get 6, adding 2 + 4")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_calculator_initiated(self):
        self.assertIsInstance(self.calc, SimpleCalc, msg="Is it a calculator object?")


#- There should be a calculator object
# - It should add two numbers
# - It should subtract two numbers
# - It should multiply two
# - It should divide two numbers
# - Nice to have: It could keep the last result in memory.