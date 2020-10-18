# content of test_class.py
import unittest
from python.source.arrays.max_profit import Solution


class TestSolution(unittest.TestCase):
    sol = Solution()

    def test_max_profit(self):
        stocks = [7, 1, 5, 3, 6, 4]
        max_profit = self.sol.maxProfit(stocks)
        self.assertEqual(7, max_profit)

    def test_max_profit_linear(self):
        stocks = [1, 2, 3, 4, 5]
        max_profit = self.sol.maxProfit(stocks)
        self.assertEqual(4, max_profit)

    def test_no_profit(self):
        stocks = [7, 6, 4, 3, 1]
        max_profit = self.sol.maxProfit(stocks)
        self.assertEqual(0, max_profit)


if __name__ == '__main__':
    unittest.main()
