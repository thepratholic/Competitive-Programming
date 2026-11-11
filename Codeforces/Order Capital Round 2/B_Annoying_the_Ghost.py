def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        j = i

        while j < n and a[j] > b[i]:
            j += 1

        if j == n:
            ans = -1
            break

        ans += j - i
        x = a.pop(j)
        a.insert(i, x)

    print(ans)


t = int(input())
for _ in range(t):
    solve()
