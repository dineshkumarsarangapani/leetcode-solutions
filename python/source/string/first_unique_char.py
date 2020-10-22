class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        i = 0
        for x in s:
            if d[x] == 1:
                return i
            i += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    #print(s.firstUniqChar("lee"))
    #print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("dddccdbba"))
