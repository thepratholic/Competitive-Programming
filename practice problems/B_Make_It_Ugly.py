for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lst = -1
    ans = n
    for i in range(n):
        if a[i] != a[0]:
            ans = min(ans, i - lst - 1)
            lst = i
    ans = min(ans, n - lst - 1)
    if ans == n:
        print(-1)
    else:
        print(ans)