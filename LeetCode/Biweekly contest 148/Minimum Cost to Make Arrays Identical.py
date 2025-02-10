from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)
    
        def cost_without_rearrange():
            return sum(abs(arr[i] - brr[i]) for i in range(n))
        
        def cost_with_rearrange():
            sorted_arr = sorted(arr)
            sorted_brr = sorted(brr)
            return k + sum(abs(sorted_arr[i] - sorted_brr[i]) for i in range(n))
        
        return min(cost_without_rearrange(), cost_with_rearrange())