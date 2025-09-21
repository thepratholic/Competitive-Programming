from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = 0

        maxi = max(nums)
        mini = min(nums)

        for _ in range(k):
            ans += (maxi - mini)

        return ans