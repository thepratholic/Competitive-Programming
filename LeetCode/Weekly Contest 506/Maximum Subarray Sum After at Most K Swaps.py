from sortedcontainers import SortedList
from bisect import bisect_left

class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        sorted_nums = sorted(nums)
        ans = float('-inf')

        for start in range(n):
            others = SortedList(sorted_nums[ : max(0, n - k)])
            candidates = SortedList(sorted_nums[max(0, n - k) : ])
            cur_sum = 0

            for end in range(start, n):
                if others:
                    idx = bisect_left(others, nums[end])

                    if idx < len(others) and others[idx] == nums[end]:
                        others.pop(idx)
                        value = nums[end]

                    else:
                        value = others.pop()

                    candidates.add(value) # hum compensate kar rhe hai

                best = candidates.pop()
                cur_sum += best

                ans = max(ans, cur_sum)

        return ans