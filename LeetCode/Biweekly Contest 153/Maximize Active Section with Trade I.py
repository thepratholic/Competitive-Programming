from cmath import inf


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        maxi, cur, prev = 0, 0, -inf

        ones = s.count('1')

        for c in s:
            if c == '0':
                cur += 1

            elif c == '1' and cur > 0:
                prev = cur
                cur = 0

            if cur > 0:
                maxi = max(maxi, cur + prev)

        return maxi + ones