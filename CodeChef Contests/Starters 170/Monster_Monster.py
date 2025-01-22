# cook your dish here
for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    arr = list(map(int, input().split()))

    
    arr.sort()
    
    max_a = 0
    
    for i in range(n):
        effective_hp = arr[i] + (n - i - 1) * x
        max_a = max(max_a, effective_hp)
    
    print(max_a)