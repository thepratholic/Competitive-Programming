class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = max(nums[i], suf[i + 1])

        ans = 0

        for i in range(n - k):
            ans = max(ans, nums[i] + suf[i + k])

        return ans