from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        first = sum(nums[:k])
        last = sum(nums[-k:])
        return abs(first - last)