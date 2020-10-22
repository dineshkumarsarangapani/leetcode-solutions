from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1 and target == nums[0]:
            return [0, 0]

        left, right = 0, len(nums) - 1
        left_index = -1
        right_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_index = mid
                right_index = mid
                break
            elif nums[mid] < target:
                left = mid - 1
            else:
                right = mid + 1
        if nums[left] == target:
            left_index = left
        if nums[right] == target:
            right_index = right-1

        while nums[left_index] != target and nums[right_index] != target:
            if left_index - 1 < 0 or right_index + 1 > len(nums):
                break
            left_index -= 1
            right_index += 1

        if left_index == -1:
            return [-1, -1]

        return [left_index, right_index + 1]


if __name__ == '__main__':
    s = Solution()
    num = [5, 7, 7, 8, 8, 10]
    #num = [2, 2]
    target = 2
    #target = 6
    x = s.searchRange(num, target)
    print(x)

    6
