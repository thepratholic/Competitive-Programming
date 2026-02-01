from cmath import sqrt
from typing import List


class Solution:
    def minimumK(self, nums: List[int]) -> int:

        n = len(nums)

        def f(mid):
            cnt = 0
            for i in range(n):
                cnt += (nums[i] + mid - 1) // mid

                if cnt > mid * mid:
                    return False

            return True

        low, high = 1, max(max(nums), int(sqrt(n)) + 2)
        ans = high

        while low <= high:
            mid = (low + high) >> 1

            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
