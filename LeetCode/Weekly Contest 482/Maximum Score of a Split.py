from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        pref = [0] * n
        suf_min = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]

        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])

        score = float('-inf')
        for i in range(n - 1):
            score = max(score, pref[i] - suf_min[i + 1])

        return score