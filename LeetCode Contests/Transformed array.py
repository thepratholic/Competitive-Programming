from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [-1] * n

        for i in range(n):
            if nums[i] > 0:
                target_ind = (i + nums[i]) % n

            elif nums[i] < 0:
                target_ind = (i + nums[i]) % n

            else:
                res[i] = nums[i]
                continue

            res[i] = nums[target_ind]

        return res
