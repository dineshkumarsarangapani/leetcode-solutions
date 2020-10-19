from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1


if __name__ == '__main__':
    s = Solution()
    x = s.mySqrt(1)
    print(x)
    x = s.mySqrt(2)
    print(x)
    x = s.mySqrt(3)
    print(x)
    x = s.mySqrt(4)
    print(x)
    x = s.mySqrt(8)
    print(x)
