from typing import List
from sortedcontainers import SortedSet
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)
        nums.extend(nums)
        st = SortedSet((nums[i], i) for i in range(3 * n))

        ans = []

        for q in queries:
            q += n

            it = st.bisect_left((nums[q], q))

            prev_it = st[it - 1][1] if it > 0 else float('inf')
            next_it = st[it + 1][1] if it + 1 < len(st) else float('inf')

            ans.append(min(n, q - prev_it, next_it - q))

            if ans[-1] == n:
                ans[-1] = -1

        return ans
