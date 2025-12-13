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

def pre():
    v = []
    a = 3

    while True:
        sa = a * a
        b = sa // 2
        c = b + 1

        if c > 10**9: break

        if (b * b) + sa == (c * c) and c == sa - b:
            v.append(c)

        a += 2

    return v

def solve():
    n = int(input())
    ans = pre()

    idx = bisect_right(ans, n)

    print(idx)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()