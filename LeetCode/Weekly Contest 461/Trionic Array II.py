from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # left incremented sum storing
        left_increasing = [0] * n
        left_increasing[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left_increasing[i] = max(nums[i], left_increasing[i - 1] + nums[i])
            else:
                left_increasing[i] = nums[i]

        # right side ka sum precompute karo
        right_increasing = [0] * n
        right_increasing[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_increasing[i] = max(nums[i], right_increasing[i + 1] + nums[i])

            else:
                right_increasing[i] = nums[i]

        # find trionic check
        ans = float('-inf')
        i = 0

        while i < n:

            if i + 2 < n and nums[i] < nums[i + 1] > nums[i + 2]:
                j = i + 1
                middle_sum = 0

                while j + 1 < n and nums[j] > nums[j + 1]:
                    middle_sum += nums[j]
                    j += 1
                
                middle_sum += nums[j]

                if j + 1 < n and nums[j] < nums[j + 1]:
                    total = left_increasing[i] + middle_sum + right_increasing[j + 1]
                    ans = max(ans, total)

                i = j - 1

            i += 1

        return ans