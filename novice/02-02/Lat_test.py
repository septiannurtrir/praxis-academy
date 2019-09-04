import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([5, 5, 5]), 15, "Should be 15")
        
    def test_sum_tuple(self):
        self.assertEqual(sum([5, 4, 5]), 15, "Should be 15")
        
if __name__ == "__main__":
    unittest.main()