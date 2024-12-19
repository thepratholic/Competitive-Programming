# cook your dish here
for _ in range(int(input())):
    
    a, b, x, y = map(int, input().split())
    
    ab = a * b 
    xy = x * y
    
    if (xy >= ab):
        print("YES")
        
    else:
        print("NO")