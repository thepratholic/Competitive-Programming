from cmath import inf
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        dp = [-inf]*k
        dp[0] = prefix = max_delete = 0

        for val in nums:
            prefix += val
            r = prefix % k

            candidate = dp[r] + prefix
            max_delete = max(max_delete,candidate)
            dp[r] = max(dp[r],max_delete-prefix)
        
        return total-max_delete