class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n):
            prod = 26 - (ord(s[i]) - ord('a'))
            total += prod * (i + 1)

        return total