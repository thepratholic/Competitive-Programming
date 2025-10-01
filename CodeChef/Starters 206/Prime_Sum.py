def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    primes = {2, 3, 5}
    
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] in primes:
                cnt += 1
                
    print(cnt)

t = int(input())
for _ in range(t):
    solve()
