from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hash = {}
        min_operations = 0
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for j in hash.keys():
            if j > k:
                min_operations += 1
            if j < k:
                return -1

        return min_operations