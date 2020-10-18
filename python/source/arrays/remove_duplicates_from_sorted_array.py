from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)

        if length == 0:
            return 0

        for j in range(1, length):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1