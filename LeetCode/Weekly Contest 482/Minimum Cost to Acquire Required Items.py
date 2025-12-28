class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        res1 = need1 * cost1 + need2 * cost2

        both = min(need1, need2)

        res2 = (both * costBoth) + (need1 - both) * cost1 + (need2 - both) * cost2

        res3 = max(need1, need2) * costBoth

        return min(res1, res2, res3)