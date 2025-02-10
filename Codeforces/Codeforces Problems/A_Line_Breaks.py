def solve():
    n, m = map(int, input().split())

    l = []

    for i in range(n):
        l.append(input())

    ans = 0

    for i in range(n):
        if len(l[i]) <= m:
            ans += 1
            m -= len(l[i])
        else:
            break

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
