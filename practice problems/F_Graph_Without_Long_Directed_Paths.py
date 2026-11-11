import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
color = [-1] * (n + 1)
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    edges.append((u, v))

ok = True

for start in range(1, n + 1):
    if color[start] != -1:
        continue

    color[start] = 0
    q = deque([start])

    while q and ok:
        u = q.popleft()

        for v in g[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break

    if not ok:
        break

if not ok:
    print("NO")
else:
    print("YES")
    ans = []
    for u, _ in edges:
        ans.append(str(color[u]))
    print("".join(ans))