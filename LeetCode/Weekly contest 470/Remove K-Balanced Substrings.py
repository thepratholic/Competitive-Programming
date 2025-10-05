class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        n = len(s)

        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                
            else:
                stack.append([ch, 1])
            while (len(stack) >= 2
                and stack[-2][0] == '('
                and stack[-1][0] == ')'
                and stack[-2][1] >= k
                and stack[-1][1] >= k):
                stack[-2][1] -= k
                
                stack[-1][1] -= k
                
                if stack[-2][1] == 0 and stack[-1][1] == 0:
                    stack.pop()
                    stack.pop()
                    
                elif stack[-2][1] == 0:
                    del stack[-2]
                    
                elif stack[-1][1] == 0:
                    stack.pop()
                    
        return "".join(ch * cnt for ch, cnt in stack)