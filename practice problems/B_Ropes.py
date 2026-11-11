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
    a = []

    for _ in range(n):
        a.append(int(input()))

    low, high = 0.0, max(a)


    def check(mid):
        pieces = 0
        for x in a:
            pieces += (x // mid)

            if pieces >= k: return True

        return False

    while (high - low) > 1e-6:
        mid = low + (high - low) / 2

        if check(mid):
            low = mid
        else:
            high = mid

    print(f"{low : .6f}")

if __name__ == '__main__':
    # t = 1
    # for _ in range(t):
    solve()