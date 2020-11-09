import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = [1]
        c2 = c3 = c5 = 0
        while len(num) < n:
            next = min(2*num[c2], 3*num[c3], 5*num[c5])
            num.append(next)
            if next == 2*num[c2]:
                c2 += 1
            if next == 3*num[c3]:
                c3 += 1
            if next == 5*num[c5]:
                c5 += 1
        return num[n-1]


'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.

'''