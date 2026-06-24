def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    j = 0

    for i in range(n):
        while j < n and a[j] - a[i] <= 2:
            j += 1

        cnt = j - i - 1  # elements after i within difference <= 2

        if cnt >= 2:
            ans += cnt * (cnt - 1) // 2

    print(ans)


t = int(input())
for _ in range(t):
    solve()