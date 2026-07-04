from typing import List
from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        NEG_INF = -inf

        no_op = NEG_INF
        multiply = NEG_INF
        divide = NEG_INF
        finished = NEG_INF

        ans = NEG_INF

        for x in nums:
            mul = x * k
            div = int(x / k)

            finished = max(finished + x, multiply + x, divide + x)

            multiply = max(no_op + mul, multiply + mul, mul)

            divide = max(div, no_op + div, divide + div)

            no_op = max(no_op + x, x)

            ans = max(ans, finished, multiply, divide, no_op)

        return ans