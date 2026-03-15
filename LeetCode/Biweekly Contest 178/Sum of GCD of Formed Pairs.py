from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefgcd = [0] * n
        mx = float('-inf')

        for i in range(n):
            mx = max(mx, nums[i])
            prefgcd[i] = gcd(nums[i], mx)

        prefgcd.sort()

        ans = 0
        l, r = 0, n - 1

        while l < r:
            ans += gcd(prefgcd[l], prefgcd[r])

            l += 1
            r -= 1

        return ans