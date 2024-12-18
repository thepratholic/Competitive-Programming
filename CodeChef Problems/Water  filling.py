# cook your dish here
for _ in range(int(input())):
    
    b1, b2, b3 = map(int, input().split())
    
    total = b1 + b2 + b3
    
    if total <= 1:
        print("Water filling time")
        
    else:
        print("Not now")