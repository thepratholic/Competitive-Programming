from functools import cache


class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:

        # simple digit dp lagega
        def solve(num):
            if num < 0:
                return 0

            s = str(num)
            n = len(s)

            @cache
            def f(pos, prev, tight, start):
                if pos == n:
                    return 1

                ub = int(s[pos]) if tight else 9
                ans = 0

                for dig in range(ub + 1):
                    new_tight = tight and (dig == ub)

                    if not start:
                        if dig == 0:
                            ans += f(pos + 1, 0, new_tight, False)

                        else:
                            ans += f(pos + 1, dig, new_tight, True)

                    else:
                        if abs(prev - dig) <= k:
                            ans += f(pos + 1, dig, new_tight, True)

                return ans

            return f(0, 0, True, False)

        return solve(r) - solve(l - 1)