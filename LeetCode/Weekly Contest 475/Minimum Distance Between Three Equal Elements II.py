from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        mpp = defaultdict(list)

        for i in range(n):
            mpp[nums[i]].append(i)

        ops = float('inf')

        for k,v in mpp.items():

            cur_dist = 0
            if len(v) >= 3:

                for i in range(len(v) - 2):
                    dist = 2 * (v[i + 2] - v[i])
                    ops = min(ops, dist)

        return ops if ops != float('inf') else -1