import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years

    def test_value_returned_is_same(self):
        compound_interest = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, CompoundInterest.compound_interest_calculated(compound_interest))

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_value_returned_is_equal_to_above(self):
        compound_interest = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, CompoundInterest.compound_interest_calculated(compound_interest))

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_value_returned_is_equal_to_above_2(self):
        compound_interest = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, CompoundInterest.compound_interest_calculated(compound_interest))


    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_value_returned_is_equal_to_above_3(self):
        compound_interest = CompoundInterest(0, 10, 1)
        self.assertEqual(0.00, CompoundInterest.compound_interest_calculated(compound_interest))


    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_value_returned_is_equal_to_above_4(self):
        compound_interest = CompoundInterest(100, 0, 10)
        self.assertEqual(100.00, CompoundInterest.compound_interest_calculated(compound_interest))



    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

