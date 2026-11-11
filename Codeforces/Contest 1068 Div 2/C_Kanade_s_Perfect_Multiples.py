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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(set(a))
    n = len(a)

    vis = [True] * n
    pos = True

    for i in range(n):
        if not vis[i]:
            continue

        x = a[i]
        j = 2 * x

        while j <= k:
            idx = bisect_left(a, j)

            if idx < n and a[idx] == j:
                vis[idx] = False

            else:
                pos = False
                break

            j += x

        if not pos: break

    if not pos:
        print(-1)
        return
    
    res = [a[i] for i in range(n) if vis[i]]
    print(len(res))
    print(*res)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()