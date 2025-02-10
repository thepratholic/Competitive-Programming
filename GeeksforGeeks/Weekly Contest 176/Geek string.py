class Solution:
    def hasGeekSubsequence(self, s : str) -> bool:
        # code here
        target = "geek"
        j=0

        for i in range(len(s)):
            if s[i] == target[j]: j+=1
            if j == len(target): return True
        return False