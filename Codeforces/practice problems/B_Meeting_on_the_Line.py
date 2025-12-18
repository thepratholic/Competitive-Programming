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
    pos = list(map(int, input().split()))
    times = list(map(int, input().split()))

    def check(t):
        left, right = -1e18, 1e18

        for i in range(n):
            if times[i] > t: return False

            left = max(left, pos[i] - (t - times[i]))
            right = min(right, pos[i] + (t - times[i]))

        return left <= right
    

    low, high = 0, 2e18
    ans = -1

    while high - low > 1e-6:
        mid = low + (high - low) / 2

        if check(mid):
            ans = mid
            high = mid

        else:
            low = mid

    left, right = -1e18, 1e18
    t = high
    for i in range(n):
        if times[i] > t: return False

        left = max(left, pos[i] - (t - times[i]))
        right = min(right, pos[i] + (t - times[i]))

    print(f"{(left + right) / 2}")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()