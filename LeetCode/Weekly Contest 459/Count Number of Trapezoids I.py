from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_groups = defaultdict(int)

        for x, y in points:
            y_groups[y] += 1

        res = total = 0

        for y, count in y_groups.items():
            lines = count * (count - 1) // 2
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD

        return res