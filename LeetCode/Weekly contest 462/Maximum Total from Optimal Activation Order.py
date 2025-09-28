from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        mpp = defaultdict(list)

        for i in range(n):
            heapq.heappush(mpp[limit[i]], value[i])
            if len(mpp[limit[i]]) > limit[i]:
                heapq.heappop(mpp[limit[i]])

        ans = 0
        for best in mpp.values():
            ans += sum(best)

        return ans