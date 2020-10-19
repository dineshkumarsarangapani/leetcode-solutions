# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

def guess(n):
    if n == 6:
        return 0
    elif n < 6:
        return -1
    else:
        return 1
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        ## handling edge cases
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n

        while left <= right:
            mid = (left + right) // 2
            guess_num = guess(mid)
            if guess_num == 0:
                return mid
            elif guess_num == -1:
                right = mid - 1
            elif guess_num == 1:
                left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    s.guessNumber(6)
