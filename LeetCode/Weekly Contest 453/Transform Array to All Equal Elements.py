from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def min_ops_to_make_all(target):
            arr = nums[:]
            ops = 0
            for i in range(len(arr) - 1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i + 1] *= -1
                    ops += 1
            if all(x == target for x in arr):
                return ops
            return float('inf') 

        return min(min_ops_to_make_all(1), min_ops_to_make_all(-1)) <= k