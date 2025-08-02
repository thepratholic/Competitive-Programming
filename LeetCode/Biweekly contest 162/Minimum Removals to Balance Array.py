from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        left = 0

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len