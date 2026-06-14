from typing import List


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m = len(units)
        n = len(units[0])
        if n == 1:
            return sum(row[0] for row in units)

        v = []
        for row in units:
            row.sort()
            v.append((row[1], row[0]))

        v.sort()
        ans = 0
        mn = v[0][1]

        for i in range(1, m):
            ans += v[i][0]
            mn = min(mn, v[i][1])
            
        return ans + mn