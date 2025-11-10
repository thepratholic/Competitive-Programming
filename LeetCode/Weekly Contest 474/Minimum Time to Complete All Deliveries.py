from math import lcm
from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        

        def f(mid):
            req_d1 = mid - (mid // r[0])
            req_d2 = mid - (mid // r[1])
            for_both = mid - (mid // lcm(r[0], r[1]))

            return req_d1 >= d[0] and req_d2 >= d[1] and for_both >= sum(d)


        low = sum(d)
        high = int(1e12)
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans