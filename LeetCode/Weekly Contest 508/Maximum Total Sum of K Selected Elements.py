class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        ans = 0
        i = len(nums) - 1
        
        while k > 0:
            if mul > 1:
                ans += (nums[i] * mul)

            else:
                ans += nums[i]

            k -= 1
            i -= 1
            mul -= 1

        return ans