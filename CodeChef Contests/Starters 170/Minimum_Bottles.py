# cook your dish here
for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    total_water = sum(arr)
    
    bottles = (total_water + x - 1) // x
            
    print(bottles)