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

def check(z, y, x, k):
    for i in range(1, x + 1):
        z = z - (z // y)

    return z >= k

def solve():
    x, y, k = map(int, input().split())

    low, high = 0, 10 ** 12
    ans = -1

    while low <= high:
        mid = (low + high) >> 1

        if check(mid, y, x, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()