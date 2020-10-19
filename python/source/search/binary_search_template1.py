from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1

        left = 0  ## First element
        right = length - 1  ## last element
        while (left <= right):  ## traversal is ended
            middle = (left + right) // 2  ## find the mid element
            a = nums[middle]
            if a == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 4, 12, 545, 12, 14]
    nums.sort()
    index = s.search(nums, 545)
    print(index)
