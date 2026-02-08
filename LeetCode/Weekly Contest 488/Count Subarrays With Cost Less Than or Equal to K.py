from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        maxi_q = deque()
        mini_q = deque()

        l = 0
        ans = 0

        for r in range(n):
            while maxi_q and maxi_q[-1] < nums[r]:
                maxi_q.pop()

            maxi_q.append(nums[r])

            while mini_q and mini_q[-1] > nums[r]:
                mini_q.pop()

            mini_q.append(nums[r])

            while (maxi_q[0] - mini_q[0]) * (r - l + 1) > k:
                if nums[l] == mini_q[0]:
                    mini_q.popleft()

                if nums[l] == maxi_q[0]:
                    maxi_q.popleft()

                l += 1

            ans += (r - l + 1)

        return ans