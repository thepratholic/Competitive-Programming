from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = 0
            for j in range(i, n):
                if nums[j] == target: freq += 1

                l = j - i + 1
                if freq > l // 2: ans += 1
        return ans