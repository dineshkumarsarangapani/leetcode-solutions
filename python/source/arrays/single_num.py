from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd_element = 0
        for i in nums:
            odd_element ^= i

        return odd_element