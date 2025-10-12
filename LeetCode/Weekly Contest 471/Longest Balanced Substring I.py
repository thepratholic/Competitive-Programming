from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        ans = 0

        for i in range(n):
            freq = defaultdict(int)

            for j in range(i, n):
                freq[s[j]] += 1

                vals = list(freq.values())

                if len(set(vals)) == 1:
                    ans = max(ans, j - i + 1)

        return ans