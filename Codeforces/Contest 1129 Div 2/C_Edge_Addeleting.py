import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    # n = int(input())
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * (n + 1)
    dist[n] = 0
    q = deque([n])

    while q:
        u = q.popleft()

        for nei in adj[u]:
            if nei != 1 and dist[nei] < 0:
                dist[nei] = dist[u] + 1
                q.append(nei)

    best = 0

    for nei in adj[1]:
        if dist[nei] >= 0:
            best = dist[nei]
            break

    s = list(map(int, input().split()))
    for node in s:
        if dist[node] > best:
            best = dist[node]

    print(best + 1)
    

t = int(input())
for _ in range(t):
    solve()