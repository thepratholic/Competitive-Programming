from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs, triplets = set(), set()

        for i, val in enumerate(nums):
            for x in nums[i :]:
                pairs.add(val ^ x)

        for xy in pairs:
            for z in nums:
                triplets.add(xy ^ z)

        return len(triplets)