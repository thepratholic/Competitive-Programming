from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        n = len(nums)

        binary = []
        for i in range(n):
            b = bin(nums[i])[2:][::-1]
            ref = int(b, 2)
            binary.append((ref, nums[i], i))

        binary.sort(key = lambda x : (x[0], x[1]))

        ans = []
        for i in range(n):
            ans.append(nums[binary[i][2]])

        return ans