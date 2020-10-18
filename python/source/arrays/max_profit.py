from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer soltion
        length = len(prices)

        if length == 0:
            return 0

        max_profit = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit