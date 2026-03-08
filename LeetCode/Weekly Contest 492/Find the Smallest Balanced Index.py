class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)

        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]

        # suff = [1] * n
        # suff[-1] = nums[-1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = suff[i + 1] * nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            left = pref[i - 1] if i > 0 else 0

            if left == right:
                return i

            right *= nums[i]

        return -1