from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_groups = defaultdict(list)

        for x, y in points:
            y_groups[y].append(x)

        segment_counts = []
        for x_list in y_groups.values():
            count = len(x_list)
            if count >= 2:
                segment_counts.append(count * (count - 1) // 2)

        total = sum(segment_counts)
        square_sum = sum(c * c for c in segment_counts)

        result = (total * total - square_sum) // 2
        return result % MOD