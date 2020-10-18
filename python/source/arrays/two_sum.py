from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        sums = {}
        for j in range(0, length):
            diff = target - nums[j]
            if diff in sums:
                return [sums[diff], j]
            else:
                sums[nums[j]] = j
        


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    nums = [3, 3]
    target = 6
    nums = [3, 2, 4]
    target = 6
    index = s.twoSum(nums, target)
    print(index)
