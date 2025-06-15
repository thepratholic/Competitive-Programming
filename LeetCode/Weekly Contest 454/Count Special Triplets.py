from collections import Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        leftCount = Counter()
        rightCount = Counter(nums)
        ans = 0
    
        for j in range(len(nums)):
            rightCount[nums[j]] -= 1
    
            x = nums[j] * 2
            countLeft = leftCount[x]
            countRight = rightCount[x]
    
            ans = (ans + countLeft * countRight) % MOD
    
            leftCount[nums[j]] += 1
    
        return ans