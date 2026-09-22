from functools import cache
from typing import List


class Solution:
    def maxValue(self, a: List[int]) -> int:
        n = len(a)

        @cache
        def f(i, state):
            if i == n:
                return 0

            now = -a[i] if i & 1 else a[i]

            if state == 0:
                ans = f(i + 1, 0) + now

                if i + 1 < n:
                    if i & 1:
                        change = a[i] - a[i + 1]

                    else:
                        change = -a[i] + a[i + 1]

                    ans = max(ans, f(i + 2, 1) + change)

                return ans

            if state == 1:
                ans = f(i + 1, 2) + now

                if i + 1 < n:
                    if i % 2 == 0:
                        change = -a[i] + a[i + 1]
                    else:
                        change = a[i] - a[i + 1]

                    ans = max(ans, f(i + 2, 1) + change)

                return ans

            return f(i + 1, 2) + now

        return f(0, 0)