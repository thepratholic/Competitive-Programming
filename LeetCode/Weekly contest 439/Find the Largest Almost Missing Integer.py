from collections import defaultdict
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = defaultdict(int)
        for i in range(n - k + 1):
            
            current = set()
            for j in range(i, i + k):
                current.add(nums[j])
            
            for num in current:
                mpp[num] += 1
        
        largest = -1
        for num, count in mpp.items():
            if count == 1:
                largest = max(largest, num)
        
        return largest