from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        ans = 2

        left = [2] * n
        right = [2] * n

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                left[i] = left[i - 1] + 1

            
        for i in range(n - 3, -1, -1):
            if nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]:
                right[i] = right[i + 1] + 1

        for i in range(n):
            ans = max(ans, left[i], right[i])

            if i == 0:
                ans = max(ans, 1 + right[i + 1])

            elif i == n - 1:
                ans = max(ans, 1 + left[i - 1])

            else: # merge case
                ans = max(ans, 1 + left[i - 1])
                ans = max(ans, 1 + right[i + 1])

                diff = nums[i + 1] - nums[i - 1]

                if diff % 2 == 0:
                    req = diff // 2

                    left_len = 1
                    right_len = 1

                    if i >= 2 and nums[i - 1] - nums[i - 2] == req:
                        left_len = left[i - 1]

                    if i < n - 2 and nums[i + 2] - nums[i + 1] == req:
                        right_len = right[i + 1]

                    ans = max(ans, 1 + left_len + right_len)

        return ans