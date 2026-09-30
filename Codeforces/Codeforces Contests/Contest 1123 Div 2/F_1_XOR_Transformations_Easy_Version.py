from sys import stdin

input = stdin.readline


def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    queries = [int(input()) for _ in range(q)]

    ans = []

    while True:

        ans.append(max(a) - min(a))

        nxt = []

        for i in range(n):
            for j in range(i + 1, n):
                nxt.append(a[i] ^ a[j])

        nxt.sort()
        nxt = nxt[:n]

        if a == nxt:
            break

        a = nxt

    for k in queries:
        if k < len(ans):
            print(ans[k])
        else:
            print(ans[-1])


t = int(input())

for _ in range(t):
    solve()