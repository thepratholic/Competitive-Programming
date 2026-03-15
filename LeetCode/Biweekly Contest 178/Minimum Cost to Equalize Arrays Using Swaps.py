from typing import Counter


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        freq = Counter(nums1)

        for i in range(n):
            freq[nums2[i]] -= 1

        ans = 0
        for v in freq.values():
            if v % 2 != 0:
                return -1

            ans += abs(v)

        return ans // 4