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

def query(l, r):
    print("? ", l, r, flush=True)
    s = int(input())
    return (r - l + 1) - s

def solve():
    n, t = map(int, input().split())
    k = int(input())

    low, high = 1, n
    ans = n

    while low <= high:
        mid = (low + high) >> 1

        res = query(1, mid)
        
        if res >= k:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    print("! ", ans, flush=True)


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()