# cook your dish here
for _ in range(int(input())):
    
    d, l, r = map(int, input().split())
    
    if d >= l and d <= r:
        print("Take second dose now")
        
    elif d > l and d > r:
        print("Too Late")
        
    else:
        print("Too Early")
        