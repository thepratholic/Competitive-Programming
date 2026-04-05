from collections import defaultdict


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        cnt = defaultdict(int)

        a = 1
        while a ** 3 < n:
            b = a

            while a ** 3 + b ** 3 <= n:
                cnt[a ** 3 + b ** 3] += 1
                b += 1

            a += 1

        return sorted(x for x, ct in cnt.items() if ct > 1)