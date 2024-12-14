from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0

        def simulate(start, direction):
            nums_copy = nums[:]
            curr = start
            while 0 <= curr < n:
                if nums_copy[curr] > 0:
                    nums_copy[curr] -= 1
                    direction *= -1
                curr += direction
            return all(x == 0 for x in nums_copy)


        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):
                    valid_count += 1
                if simulate(i, -1):
                    valid_count += 1

        return valid_count