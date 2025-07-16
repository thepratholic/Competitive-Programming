def solve(s):
    stack = []
    
    for char in s:
        stack.append(char)
        
        while len(stack) >= 3:
            if stack[-3] != stack[-2] and stack[-2] != stack[-1]:
                stack.pop(-2)
            else:
                break
    
    return len(stack)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(solve(s))