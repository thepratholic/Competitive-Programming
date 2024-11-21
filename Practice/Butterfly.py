t = int(input())
for _ in range(t):
    r, g, b = map(int, input().split())
    
    if max(r, g, b) <= (r + g + b) - max(r, g, b):
        print("YES")
    else:
        print("NO")
