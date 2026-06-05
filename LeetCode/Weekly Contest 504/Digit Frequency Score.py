from typing import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)

        f = Counter(n)

        ans = 0

        for k, v in f.items():
            ans += (int(k) * v)

        return ans