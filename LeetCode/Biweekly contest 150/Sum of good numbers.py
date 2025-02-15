from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        good_sum = 0
        
        for i in range(n):
            is_good = True
            
            if i - k >= 0:
                if nums[i] <= nums[i-k]:
                    is_good = False
                    
            if i + k < n:
                if nums[i] <= nums[i+k]:
                    is_good = False
                    
            if is_good:
                good_sum += nums[i]
        
        return good_sum