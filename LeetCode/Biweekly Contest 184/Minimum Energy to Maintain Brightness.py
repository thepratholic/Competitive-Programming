from math import ceil


class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:

        # it heated my ide
        bulbs = min(ceil(brightness / 3), ceil(n / 3))

        intervals.sort()
        merged = [[intervals[0][0], intervals[0][1]]]

        for s, e in intervals[1:]:
            if s <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s, e])

        return bulbs * sum(e - s + 1 for s, e in merged)