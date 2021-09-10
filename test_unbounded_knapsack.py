"""
Created on Tue Aug 31 16:31:07 2022

This file contains the test-suite for the unbounded_knapsack problem.
"""
import unittest

from unbounded_knapsack.unbounded_knapsack import unbounded_knapsack


class Test(unittest.TestCase):
    def test_base_case(self):
        """
        test for the base case
        """
       
        self.assertEqual(unbounded_knapsack(capacity=0, weight=[0], value=[0], length=1), 0)

        
        self.assertEqual(unbounded_knapsack(capacity=5, weight=[10], value=[60], length=1), 0)

    def test_easy_case(self):
        """
        test for the base case
        """
        
        self.assertEqual(unbounded_knapsack(capacity=100, weight = [5, 10, 15], value = [10, 30, 20], length=3), 300)

    def test_knapsack(self):
        """
        test for the knapsack
        """
       
        self.assertEqual(unbounded_knapsack(capacity=8, weight = [1, 3, 4, 5], value = [10, 40, 50, 70], length=4), 110)


if __name__ == "__main__":
    unittest.main()
