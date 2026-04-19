class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        pref = [0] * n
        suff = [0] * n

        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = max(pref[i - 1], nums[i])

        suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(suff[i + 1], nums[i])

        for idx in range(n):
            mx = pref[idx]
            mn = suff[idx]

            if mx - mn <= k:
                return idx

        return -1