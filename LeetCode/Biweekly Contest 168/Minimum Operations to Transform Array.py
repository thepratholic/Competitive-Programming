from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        n1 = len(nums2)

        ops = 0
        for i in range(n):
            ops += abs(nums1[i] - nums2[i])


        close_val = -1
        close_diff = float('inf')
        last = nums2[-1]

        for i in range(n):
            if abs(last - nums1[i]) < close_diff:
                close_diff = abs(last - nums1[i])
                close_val = nums1[i]

            if abs(last - nums2[i]) < close_diff:
                close_diff = abs(last - nums2[i])
                close_val = nums2[i]
                
            if nums1[i] <= last <= nums2[i] or nums2[i] <= last <= nums1[i]:
                close_val = last
                close_diff = 0

        return ops + abs(last - close_val) + 1