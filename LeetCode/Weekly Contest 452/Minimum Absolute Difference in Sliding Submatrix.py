from itertools import groupby
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                sub_matrix = []

                for ix in range(i, i + k):
                    for jx in range(j, j + k):
                        sub_matrix.append(grid[ix][jx])

                sub_matrix.sort()

                unique_vals = [key for key, _ in groupby(sorted(sub_matrix))]

                if len(unique_vals) == 1:
                    row.append(0)
                else:
                    min_diff = float('inf')
                    for l in range(1, len(unique_vals)):
                        min_diff = min(min_diff, unique_vals[l] - unique_vals[l - 1])
                    row.append(min_diff)
            ans.append(row)

        return ans