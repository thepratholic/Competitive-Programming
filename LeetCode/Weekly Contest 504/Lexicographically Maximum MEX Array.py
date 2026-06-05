from collections import Counter

class Solution:
    def maximumMEX(self, nums):
        freq = Counter(nums)
        
        ans = []
        seen = set()
        missing = 0   # current mex in segment
        
        for x in nums:
            seen.add(x)
            freq[x] -= 1
            
            while missing in seen:
                missing += 1
            
            if missing not in freq or freq[missing] == 0:
                ans.append(missing)
                
                seen.clear()
                missing = 0
        
        return ans