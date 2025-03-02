from typing import List


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)

        lower, upper = bounds[0]

        for i in range(1, n):
            diff = original[i] - original[i-1]
            lower = max(lower + diff, bounds[i][0])
            upper = min(upper + diff, bounds[i][1])

            if lower > upper:
                return 0

        return upper - lower + 1