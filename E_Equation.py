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

from numpy import double
input = sys.stdin.readline



def solve():
    C = float(input())

    low, high = 0.0, sqrt(C)

    def check(mid):
        return (mid * mid) + sqrt(mid) >= C

    while high - low > -1e6:
        mid = low + (high - low) / 2

        if check(mid):
            high = mid

        else:
            low = mid

    print(f"{low:.6f}")

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()