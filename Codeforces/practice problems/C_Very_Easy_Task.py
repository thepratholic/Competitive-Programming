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
    n, x, y = map(int, input().split())

    if n == 1:
        print(min(x, y))
        return

    low, high = 1, max(x, y) * n
    ans = -1

    def check(mid):
        return (mid // x) + (mid // y) >= n - 1

    while low <= high:
        mid = (low + high) >> 1

        if check(mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    print(ans + min(x, y))

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()