from functools import lru_cache
from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def f(idx, cur_xor):
            if idx == n:
                if cur_xor == target:
                    return 0

                else:
                    return float('inf')


            keep = f(idx + 1, cur_xor ^ nums[idx])
            remove = 1 + f(idx + 1, cur_xor)

            return min(keep, remove)

        ans = f(0, 0)
        return ans if ans != float('inf') else -1