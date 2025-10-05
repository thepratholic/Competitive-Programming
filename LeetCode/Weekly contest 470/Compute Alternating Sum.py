from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0

        cnt = 0

        for i in nums:
            if cnt & 1:
                ans -= i

            else:
                ans += i

            cnt += 1

        return ans