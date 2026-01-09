from collections import defaultdict
from typing import List


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')

        mpp = defaultdict(int)

        l = 0
        cur = 0
        for r in range(n):
            mpp[nums[r]] += 1

            cur += nums[r] if mpp[nums[r]] == 1 else 0

            while cur >= k:
                ans = min(ans, r - l + 1)
                
                mpp[nums[l]] -= 1
                if mpp[nums[l]] == 0:
                    cur -= nums[l]
                    del mpp[nums[l]]
                l += 1

        return ans if ans != float('inf') else -1