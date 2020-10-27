import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_sum = best_sum = ~sys.maxsize
        for i in range(0, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            best_sum = max(current_sum, best_sum)
        return best_sum


if __name__ == '__main__':
    s = Solution()
    s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
