t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)

    s = 0

    for i in range(n):
        if a[i] * (1 << s) <= c:
            s += 1

    print(n - s)