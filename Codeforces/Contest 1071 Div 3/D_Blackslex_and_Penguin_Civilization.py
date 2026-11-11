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
    n = int(input())
    lim = 1 << n

    vis = [False] * lim
    ans = []
    for i in range(n, -1, -1):
        mask = (1 << i) - 1

        for j in range(lim):
            if not vis[j] and (j & mask) == mask:
                vis[j] = True
                ans.append(j)

    print(*ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()