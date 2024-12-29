
from typing import List

class Solution:
    def minCost(self, n : int, a : List[int]) -> int:

        cost_to_even = 0

        cost_to_odd = 0

        for x in a:
            if x % 2 == 0:
                cost_to_odd += x
            else:
                cost_to_even += x

        return min(cost_to_even, cost_to_odd)