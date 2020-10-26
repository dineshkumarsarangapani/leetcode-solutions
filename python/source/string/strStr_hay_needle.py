class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        needle_length = len(needle)
        haystack_len = len(haystack)
        if needle_length == 0 and haystack_len == 0:
            return 0
        j = 0
        for c in haystack:
            if needle[i] == c:
                #while i <= needle_length:
                pass

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", 'll'))
    print(s.strStr("helo", 'll'))
