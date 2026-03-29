class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)

        for i in range(len(s) + 1 // 2):
            if s[i] == s[n - i - 1]:
                return i

        return -1