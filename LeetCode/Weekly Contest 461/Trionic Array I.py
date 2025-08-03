from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 3:
            return False

            
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
    
        p = i
        if p == 0 or p == n - 1:
            return False
    
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
    
        q = i
        if q == p or q == n - 1:
            return False 
    
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
    
        return i == n - 1