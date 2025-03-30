class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str, t: str) -> int:
        max_len = 0
        n = len(s)
        for i in range(n + 1): 
            for j in range(i, n + 1):  
                sub_s = s[i:j]
                m = len(t)
                for k in range(m + 1): 
                    for l in range(k, m + 1):  
                        sub_t = t[k:l]
                        candidate = sub_s + sub_t
                        if candidate and self.is_palindrome(candidate):
                            max_len = max(max_len, len(candidate))
        return max_len