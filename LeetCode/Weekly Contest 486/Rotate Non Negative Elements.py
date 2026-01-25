from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        pos = []
        vals = []
        for i, val in enumerate(nums):
            if val >= 0:
                pos.append(i)
                vals.append(val)

        m = len(vals)
        if m == 0:
            return nums

        k = k % m
        vals = vals[k:] + vals[:k]

        res = nums[:]
        for i, val in zip(pos, vals):
            res[i] = val

        return res