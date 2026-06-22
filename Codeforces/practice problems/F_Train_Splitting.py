import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    edges = []
    adj = [[] for _ in range(n + 1)]

    complete = (m == n * (n - 1) // 2)

    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))


        if not (i == 0 and complete):
            adj[u].append(v)
            adj[v].append(u)

    junction = 1

    for i in range(1, n + 1):
        s = {i}
        for nxt in adj[i]:
            s.add(nxt)

        if len(s) != n:
            junction = i

    k = 3 if complete else 2
    print(k)

    ans = []

    for i, (u, v) in enumerate(edges):
        if complete and i == 0:
            ans.append(3)
        elif u == junction or v == junction:
            ans.append(1)
        else:
            ans.append(2)

    print(*ans)