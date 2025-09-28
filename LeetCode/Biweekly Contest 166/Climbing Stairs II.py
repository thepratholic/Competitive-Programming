from cmath import inf
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        n = len(costs)
        

        dp = [inf] * (n + 1)
        dp[0] = 0 

        for i in range(n): 
            for jump in [1, 2, 3]:
                j = i + jump
                if j <= n:
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + (j - i) ** 2)


        return dp[n]