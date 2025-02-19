# cook your dish here

x, y = map(int, input().split())

ans = x + (y * 10)

if ans >= 100:
    print("YES")
    
else: print("NO")