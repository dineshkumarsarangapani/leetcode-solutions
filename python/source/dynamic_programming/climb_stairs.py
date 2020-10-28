class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 1
        for i in range(1, n):
            first, second = second, first + second

        return second