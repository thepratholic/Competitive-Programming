from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)

        suf = [False] * n
        suf[-1] = True

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                suf[i] = True

            else:
                break

        for i in range(n - 1, -1, -1):
            if not suf[i]:
                return i + 1

        return 0