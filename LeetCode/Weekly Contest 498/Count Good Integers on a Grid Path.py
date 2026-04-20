from functools import lru_cache


class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        path = {0}
        pos = 0

        for d in directions:
            if d == 'D':
                pos += 4

            else:
                pos += 1

            path.add(pos)

        
        def solve(x):
            s = str(x).zfill(16)

            @lru_cache(None)
            def f(idx, last, tight):
                if idx == 16:
                    return 1

                ub = int(s[idx]) if tight else 9
                res = 0

                for digit in range(ub + 1):

                    if idx in path:

                        if digit >= last:
                            res += f(idx + 1, digit, tight and (digit == ub))

                    else:
                        res += f(idx + 1, last, tight and (digit == ub))

                return res

            return f(0, 0, True)

        return solve(r) - solve(l - 1)