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
    a = []
    b = []

    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    def f(mid):
        p = 0
        for i in range(n):
            if p <= b[i] and (mid - p - 1) <= a[i]:
                p += 1

        return p >= mid

    ans = -1
    low, high = 0, n

    while low <= high:
        mid = (low + high) >> 1

        if f(mid):
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()