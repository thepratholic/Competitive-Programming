from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 0]

        def f(parity):
            points = []
            ops = 0

            for i, x in enumerate(nums):
                if (x + i) % 2 == parity:
                    points.append((x, i))

                else:
                    ops += 1
                    points.append((x - 1, i))
                    points.append((x + 1, i))

            points.sort()
            cnt = [0] * n
            covered = l = 0
            best = 10 ** 20

            for r in range(len(points)):
                val, idx = points[r]
                covered += (cnt[idx] == 0)
                cnt[idx] += 1

                while covered == n:
                    v, i = points[l]
                    best = min(best, val - v)
                    cnt[i] -= 1
                    covered -= (cnt[i] == 0)
                    l += 1

            return ops, best

        return min(f(0), f(1))