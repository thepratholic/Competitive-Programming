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

def ask(l, r):
    print("? ", l, r, flush=True)
    v = list(map(int, input().split()))
    return v

def solve():
    n = int(input())

    low, high = 1, n
    ans = -1
    while low <= high:
        mid = (low + high) >> 1

        v = ask(low, mid)
        cnt = 0

        for val in v:
            if val >= low and val <= mid: cnt += 1

        if cnt & 1:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    
    print("! ", ans, flush=True)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()