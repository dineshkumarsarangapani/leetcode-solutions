class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x<0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev*10 + mod
        """
        Check md file
        """
        return sign*rev if -pow(2,31) <= sign*rev <= pow(2,31)-1 else 0


if __name__ == '__main__':
    s = Solution()
    a = s.reverse(123342)
    print(a)