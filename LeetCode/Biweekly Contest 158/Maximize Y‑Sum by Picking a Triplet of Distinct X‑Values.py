from collections import defaultdict
from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        vis = [False] * n
        x_map = defaultdict(int)

        for i in range(n):
            x_map[x[i]] = max(x_map[x[i]], y[i])

        top = sorted([(v, k) for k, v in x_map.items()], reverse=True)

        if len(top) < 3:
            return -1

        return top[0][0] + top[1][0] + top[2][0]