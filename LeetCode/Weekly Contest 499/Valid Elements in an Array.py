class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums
        pref = [0] * n
        suf = [0] * n

        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = max(pref[i-1], nums[i])

        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i+1], nums[i])

        ans = []

        ans.append(nums[0])
        for i in range(1, n - 1):
            if nums[i] > pref[ i- 1] or nums[i] > suf[i + 1]:
                ans.append(nums[i])

        ans.append(nums[-1])
        return ans