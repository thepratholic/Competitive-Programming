from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv = max(nums)
        B = maxv.bit_length()   
        size = 1 << B
        full = size - 1

        arr = [0] * size
        for x in nums:
            if x > arr[x]:
                arr[x] = x

        dp = arr[:]
        for b in range(B):
            bit = 1 << b
            step = bit << 1
            for start in range(bit, size, step):
                end = start + bit
                dpm = dp
                for m in range(start, end):
                    v = dpm[m - bit]
                    if v > dpm[m]:
                        dpm[m] = v

        ans = 0
        for m, val in enumerate(arr):
            if val:  
                comp = full ^ m
                cand = val * dp[comp]
                if cand > ans:
                    ans = cand
        return ans
