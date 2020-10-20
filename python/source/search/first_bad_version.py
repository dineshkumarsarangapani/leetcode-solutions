# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version == 4:
        return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            mid_res = isBadVersion(mid)
            if mid_res == False:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    mid = s.firstBadVersion(5)
