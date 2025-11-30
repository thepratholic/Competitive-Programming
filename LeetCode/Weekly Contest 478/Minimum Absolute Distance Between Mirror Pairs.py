from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        mpp = defaultdict(list)
        for i, v in enumerate(nums):
            mpp[v].append(i)

        def f(num):
            return int(str(num)[::-1])

        for i in range(n):
            new_num = f(nums[i])

            if new_num in mpp:
                l = mpp[new_num]

                j = bisect_left(l, i + 1)

                if j < len(l):
                    ans = min(ans, abs(l[j] - i))

        return ans if ans != float('inf') else -1