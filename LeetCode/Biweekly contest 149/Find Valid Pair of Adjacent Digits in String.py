class Solution:
    def findValidPair(self, s: str) -> str:
        res = ""

        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1


        for i in range(1, len(s)):

            first = s[i-1]
            second = s[i]

            if d[first] == int(first) and d[second] == int(second) and first != second:
                res = first + second
                break

        return res