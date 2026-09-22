class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        starts = sorted(l for l, r in intervals)
        ends = sorted(r for l, r in intervals)

        ans = 0

        for i, l in enumerate(starts):
            idx = bisect_left(ends, l)
            ans += i - idx

        return ans