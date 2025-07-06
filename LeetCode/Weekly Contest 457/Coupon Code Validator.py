from typing import List


class Solution:
    def isCorrectCode(self, s):
        if not s:
            return False
        for ch in s:
            if not (ch.isalnum() or ch == '_'):
                return False
        return True
        
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        s = {"electronics" : 0, "grocery" : 1, "pharmacy" : 2, "restaurant" : 3}
        n = len(code)
        ans = []
        
        for i in range(n):
            if isActive[i] and code[i] and businessLine[i] in s and self.isCorrectCode(code[i]):
                ans.append((s[businessLine[i]], code[i]))

        ans.sort()
        return [code for _, code in ans]