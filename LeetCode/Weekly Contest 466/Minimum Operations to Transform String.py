class Solution:
    def minOperations(self, s: str) -> int:
        
        max_dist = 0
        for ch in s: 
            dist = (26 - (ord(ch) - ord('a'))) % 26
            max_dist = max(max_dist, dist)
        return max_dist