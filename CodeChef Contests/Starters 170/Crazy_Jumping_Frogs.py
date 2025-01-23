# cook your dish here
for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    odd = 0
    
    for i in range(n):
        if arr[i] & 1:
            odd += 1
            
    print(max(odd, n - odd))