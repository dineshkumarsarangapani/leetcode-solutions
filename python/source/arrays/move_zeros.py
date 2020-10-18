from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        for j in range(0, length):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for x in range(i, length):
            nums[x] = 0
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    #nums = [1, 0]
    x = s.moveZeroes(nums)
    print(x)
    print(nums)
