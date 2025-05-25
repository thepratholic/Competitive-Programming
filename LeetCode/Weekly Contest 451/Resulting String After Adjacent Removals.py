class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        n = len(s)
        for i in range(len(s)):
            if i == 0:
                stack.append(s[i])
            else:
                cur = s[i]
                if stack and (abs(ord(cur) - ord(stack[-1])) == 1 or abs(ord(cur) - ord(stack[-1])) == 25):
                    stack.pop()
                else:
                    stack.append(s[i])

        return "".join(stack)