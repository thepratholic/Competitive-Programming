class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(l, r):
            nonlocal res

            while l >= 0 and r < n and s[l] == s[r]:
                r += 1
                l -= 1

            res = max(res, r - l - 1)
            return l, r

        for i in range(n):
            l, r = expand(i, i)

            expand(l - 1, r)
            expand(l, r + 1)

            l, r = expand(i, i + 1)

            expand(l - 1, r)
            expand(l, r + 1)

        return min(res, n)