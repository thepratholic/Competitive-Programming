from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        distinct, prevMax = 0, float("-inf")

        for num in nums:
            lb = num - k
            ub = num + k

            if prevMax < lb:
                prevMax = lb
                distinct += 1

            elif prevMax < ub:
                prevMax += 1
                distinct += 1

        return distinct