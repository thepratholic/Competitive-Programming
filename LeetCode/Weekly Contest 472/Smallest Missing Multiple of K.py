from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        st = set(nums)

        tmp = k
        while tmp in st:
            tmp += k

        return tmp