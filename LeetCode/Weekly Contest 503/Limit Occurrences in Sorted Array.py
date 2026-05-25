from typing import Counter


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        f = Counter(nums)

        ans = []

        for key, val in sorted(f.items()):
            ans.extend([key] * min(k, val))

        return ans