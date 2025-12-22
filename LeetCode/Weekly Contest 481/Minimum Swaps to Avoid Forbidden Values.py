from collections import Counter, defaultdict
from typing import List


class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)

        mp1 = Counter(nums)
        mp2 = Counter(forbidden)
        mp3 = defaultdict(int)
        cnt = 0

        for i in range(n):
            if nums[i] == forbidden[i]:
                cnt += 1
                mp3[nums[i]] += 1

        for k, v in mp1.items():
            if v + mp2[k] > n:
                return -1

        maxi = 0
        for k, v in mp3.items():
            maxi = max(maxi, v)

        return max(maxi, (cnt + 1) // 2)