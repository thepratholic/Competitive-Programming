from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        mx = 0

        for i in range(n):
            for j in range(i + 1, n):

                cur = (nums[i] * nums[j])
                g = gcd(nums[i], nums[j])

                mx = max(mx, cur // (g * g))

        return mx