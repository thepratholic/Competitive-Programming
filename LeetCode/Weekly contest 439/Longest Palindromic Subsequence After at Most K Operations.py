class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        
        # Memoization cache
        memo = {}
        
        def min_ops_to_match(c1, c2):
            if c1 == c2:
                return 0
                
            dist = (ord(c2) - ord(c1)) % 26
            return min(dist, 26 - dist)
        
        def dp(i, j, ops_left):
            if i > j:
                return 0
            if i == j:
                return 1
                
            state = (i, j, ops_left)
            if state in memo:
                return memo[state]
            
            result = max(dp(i + 1, j, ops_left), dp(i, j - 1, ops_left))
            
            ops_needed = min_ops_to_match(s[i], s[j])
            
            if ops_needed <= ops_left:
                result = max(result, 2 + dp(i + 1, j - 1, ops_left - ops_needed))
            
            memo[state] = result
            return result
        
        return dp(0, n - 1, k)