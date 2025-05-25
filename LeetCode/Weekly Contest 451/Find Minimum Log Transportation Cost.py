class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0

        if n > k:
            cut1 = n - k
            cut2 = n - (n - k)
            return cut1 * cut2

        if m > k:
            cut1 = m - k
            cut2 = m - (m - k)
            return cut1 * cut2