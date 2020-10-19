from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums.sort()
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
            elif nums[0] <= target < nums[middle] or (
                    # RHS is sorted [see note]
                    nums[middle] < nums[0] and
                    # target is not in RHS
                    not nums[middle] < target < nums[0]
                    # [note]: There is another possibility where RHS may be sorted, but nums[mid] ≮ nums[0]: when the array is not rotated.
                    # Still, in this case, we should search LHS' if and only if nums[0] <= target < nums[mid], so all is good.
            ):
                right = middle - 1
            else:
                left = middle + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([1], 0))
    print(s.search([1], 1))
