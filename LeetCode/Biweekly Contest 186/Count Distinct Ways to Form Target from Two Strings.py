from bisect import bisect_left
from collections import defaultdict
from functools import cache


class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n = len(word1)
        MOD = (10 ** 9) + 7

        o1 = defaultdict(list)
        o2 = defaultdict(list)

        for i, ch in enumerate(word1):
            o1[ch].append(i)

        for i, ch in enumerate(word2):
            o2[ch].append(i)

        @cache
        def f(i, j, k, msk):
            if k == len(target):
                return 1 if msk == 3 else 0

            ans = 0
            ch = target[k]

            a = o1[ch]
            idx = bisect_left(a, i)

            while idx < len(a):
                ans += f(a[idx] + 1, j, k + 1, msk | 1)
                ans %= MOD
                idx += 1

            a = o2[ch]
            idx = bisect_left(a, j)

            while idx < len(a):
                ans += f(i, a[idx] + 1, k + 1, msk | 2)
                ans %= MOD
                idx += 1

            return ans

        # msk yeh track toh kar lega ki dono strings use hui hai ya nai, if 11 hai toh yes else no

        return f(0, 0, 0, 0)