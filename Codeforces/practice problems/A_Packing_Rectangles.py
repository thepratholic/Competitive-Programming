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
    w, h, n = map(int, input().split())

    low, high = 1, w * h * n
    ans = -1

    def check(mid):
        return (mid // w) * (mid // h) >= n

    while low <= high:
        mid = (low + high) >> 1

        if check(mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    print(ans)
        

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()