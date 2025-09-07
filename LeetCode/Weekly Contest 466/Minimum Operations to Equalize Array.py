from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        target = nums[0]
        for i in range(1, len(nums)):
            
            target &= nums[i]

        for num in nums:
            if num != target:
                return 1
            
        return 0