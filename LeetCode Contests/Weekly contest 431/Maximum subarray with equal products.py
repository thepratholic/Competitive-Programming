from functools import reduce
from math import gcd
from typing import List


class Solution:
        
    def maxLength(self, nums: List[int]) -> int:
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)
    
        def array_gcd(arr):
            return reduce(gcd, arr)
        
        def array_lcm(arr):
            result = arr[0]
            for i in range(1, len(arr)):
                result = lcm(result, arr[i])
            return result
        
        def array_product(arr):
            return reduce(lambda x, y: x * y, arr)
        
        def is_product_equivalent(arr):
            product = array_product(arr)
            gcd_val = array_gcd(arr)
            lcm_val = array_lcm(arr)
            return product == lcm_val * gcd_val
        
        n = len(nums)
        max_length = 0
        
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j+1]
                if is_product_equivalent(subarray):
                    max_length = max(max_length, j - i + 1)
        
        return max_length