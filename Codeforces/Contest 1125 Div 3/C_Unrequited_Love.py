import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = {}
    ans = 0

    for i in range(n - 4):
        v = a[i] + a[i + 2] - a[i + 4]

        c = cnt.get(v, 0)
        exclude = 0

        if i >= 2:
            if v == a[i - 2] + a[i] - a[i + 2]:
                exclude += 1

        if i >= 4:
            if v == a[i - 4] + a[i - 2] - a[i]:
                exclude += 1

        ans += c - exclude
        cnt[v] = c + 1

    print(ans)


t = int(input())

for _ in range(t):
    solve()