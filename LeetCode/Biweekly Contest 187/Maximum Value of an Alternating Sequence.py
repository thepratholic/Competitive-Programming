class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s

        return s + m + (n // 2 - 1) * (m - 1)