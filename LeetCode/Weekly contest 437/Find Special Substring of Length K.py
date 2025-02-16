class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        
        if k > n:
            return False 
        
        for i in range(n - k + 1):
            sub = s[i:i + k]
            if len(set(sub)) == 1:
                before = (i == 0 or s[i - 1] != sub[0]) 
                after = (i + k == n or s[i + k] != sub[0])
                if before and after:
                    return True
        
        return False