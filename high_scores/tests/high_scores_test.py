import unittest

from src.high_scores import latest, personal_best, personal_top_three, ordered_list

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.new_list = [6, 20, 7, 5, 3, 8]

    # Test latest score (the last thing in the list)
    def test_last_thing_on_list(self): 
        self.assertEqual(8, latest(self.new_list))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(20, personal_best(self.new_list))

    # Test top three from list of scores
    def test_personal_top_3(self):
        self.assertEqual([20, 8, 7], personal_top_three(self.new_list))

    # Test ordered from highest tp lowest
    def test_sort_list(self):
        self.assertEqual([20, 8, 7, 6, 5, 3], ordered_list(self.new_list))

    # Test top three when there is a tie
    def test_top_3_when_tied(self):
        tied_list = [20, 5, 6, 20, 8, 9]
        self.assertEqual([20,20,9], personal_top_three(tied_list))

    # Test top three when there are less than three
    def test_top_3_when_less_than_3(self):
        latest_list = [20,7]
        self.assertEqual([20,7], personal_top_three(latest_list))

    # Test top three when there is only one
    def test_top_3_when_only_one(self):
        latest_list = [20]
        self.assertEqual([20], personal_top_three(latest_list))
    
