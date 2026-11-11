t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    current_max = a[0]
    
    for i in range(1, n):
        if (a[i] > 0 and current_max > 0) or (a[i] < 0 and current_max < 0):
            current_max = max(current_max, a[i])
        else:
            ans += current_max
            current_max = a[i]
    
    ans += current_max
    print(ans)