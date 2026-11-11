# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    adj = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)


    q = deque()
    q.append(1)

    
    dist = [float('inf')] * (n + 1)

    dist[1] = 0

    while q:
        cur = q.popleft()

        for adjNode in adj[cur]:
            if dist[adjNode] == float('inf'):
                q.append(adjNode)
                dist[adjNode] = dist[cur] + 1


    ans = [0] * (k + 1)

    for i in range(1, n + 1):
        ans[a[i]] = max(ans[a[i]], dist[i]) 

    print(*ans[1:k+1])



if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()