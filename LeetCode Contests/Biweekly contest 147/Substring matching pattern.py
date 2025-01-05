class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
    
        if len(prefix) + len(suffix) > len(s):
            return False
            
        def canMatch(s: str, prefix: str, suffix: str) -> bool:
            if not s.startswith(prefix):
                return False
                
            for i in range(len(prefix), len(s) - len(suffix) + 1):

                if s[i:i + len(suffix)] == suffix:
                    return True
            return False
        
        for i in range(len(s)):
            if canMatch(s[i:], prefix, suffix):
                return True
        
        return False