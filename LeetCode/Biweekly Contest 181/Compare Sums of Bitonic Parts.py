class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)

        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] += (pref[i - 1] + nums[i])

        suff = [0] * n
        suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff[i] += (suff[i + 1] + nums[i])

        peak = -1
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peak = i
                break

        asc = pref[peak]
        desc = suff[peak]

        if asc > desc:
            return 0

        elif desc > asc:
            return 1

        else:
            return -1