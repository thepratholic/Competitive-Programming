from typing import List


class Solution:
    def kLargestElements(self, arr, k):
        if k <= 0:
            return []
        if k >= len(arr):
            return sorted(arr, reverse=True)

        return sorted(arr, reverse=True)[:k]

    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maximum_elements = []

        n = len(grid)

        for i in range(n):
            tmp = grid[i]
            tmp_k = limits[i]
            maximum_elements.extend(self.kLargestElements(tmp, tmp_k))


        maximum_elements.sort(reverse=True)
        return sum(maximum_elements[:k])