# content of test_class.py
import unittest
from python.source.arrays.remove_duplicates_from_sorted_array import Solution


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        test = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        sol = Solution()
        num = sol.removeDuplicates(test)
        self.assertEqual(num, 5)
        self.assertEqual(test[0:5], [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()