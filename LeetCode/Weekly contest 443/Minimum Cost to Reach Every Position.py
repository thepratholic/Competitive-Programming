from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [-1] * n

        ans[0] = cost[0]
        for i in range(1, n):
            if cost[i] < ans[i - 1]:
                ans[i] = cost[i]

            else:
                ans[i] = ans[i - 1]

        return ans