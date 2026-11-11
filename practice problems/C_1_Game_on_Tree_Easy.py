# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple



import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, t = map(int, input().split())

    adj = defaultdict(list)
    paired = [-1] * n

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, parent):
        for adjNode in adj[u]:
            if adjNode == parent: continue

            dfs(adjNode, u)

            if paired[adjNode] == -1 and paired[u] == -1:
                paired[adjNode] = u
                paired[u] = adjNode

    dfs(0, -1)

    seen = [False] * n
    q = deque()

    for i in range(n):
        if paired[i] == -1:
            q.append(i)
            seen[i] = True

    
    while q:
        cur = q.popleft()

        for nei in adj[cur]:
            his_nei = paired[nei]

            if his_nei == -1 or seen[his_nei]:
                continue

            q.append(his_nei)
            seen[his_nei] = True

    for _ in range(t):
        x = int(input())

        if seen[x - 1]:
            print("Hermione")
        else:
            print("Ron")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()