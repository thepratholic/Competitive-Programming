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

    while n > 0:
        p, s = map(int, input().split())

        a.append((p, s))
        n -= 1


    def check(t):
        left, right = -1e18, 1e18

        for p, s in a:
            left = max(left, p - (s * t))
            right = min(right, p + (s * t))

        return left <= right
    
    low, high = 0, 2e14
    ans = -1

    while high - low > 1e-6:
        mid = low + (high - low) / 2

        if check(mid):
            ans = mid
            high = mid

        else:
            low = mid

    print(f"{ans}")

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()