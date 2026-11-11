def solve():
    n, m = map(int,input().split())

    ok = True

    p = [0] * n

    for i in range(n):
        a = list(map(int, input().split()))

        a.sort()

        if all(a[i + 1] - a[i] == n for i in range(m - 1)):
            p[a[0]] = i + 1

        else:
            ok = False

    if ok:
        print(*p)
    else:
        print(-1)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()