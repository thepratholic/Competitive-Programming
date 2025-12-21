from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)

        total_cost = sum(cost)
        char_cost = defaultdict(int)

        for i in range(n):
            char_cost[s[i]] += cost[i]

        ans = float('inf')

        for c in char_cost:
            ans = min(ans, total_cost - char_cost[c])

        return ans