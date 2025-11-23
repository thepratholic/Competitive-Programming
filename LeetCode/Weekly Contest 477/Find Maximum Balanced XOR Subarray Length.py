from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
            
        if n == 1:
            return 0
        
        ans = 0
        xr = 0
        bal = 0  # even - odd
        
        mpp = {(0, 0): -1}
        
        for i in range(n):
            xr ^= nums[i]
            
            if nums[i] % 2 == 0:
                bal += 1
            else:
                bal -= 1
            
            state = (xr, bal)
            
            if state in mpp:
                ans = max(ans, i - mpp[state])
            else:
                mpp[state] = i
        
        return ans