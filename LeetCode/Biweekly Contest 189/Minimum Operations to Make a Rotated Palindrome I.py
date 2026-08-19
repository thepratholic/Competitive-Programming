class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans = float('inf')

        for k in range(n):
            t = s[k:] + s[:k]
            cost = k

            for i in range(n // 2):
                a, b = ord(t[i]) - 97, ord(t[n - 1 - i]) - 97
                cost += min((a - b) % 26, (b - a) % 26)

            ans = min(ans, cost)

        return ans