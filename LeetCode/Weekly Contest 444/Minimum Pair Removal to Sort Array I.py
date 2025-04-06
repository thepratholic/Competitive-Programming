from typing import List


class Solution:        
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        def is_non_decreasing(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
    
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = -1
            
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    idx = i
            
            merged = nums[idx] + nums[idx+1]
            nums = nums[:idx] + [merged] + nums[idx+2:]
            
            operations += 1
        
        return operations