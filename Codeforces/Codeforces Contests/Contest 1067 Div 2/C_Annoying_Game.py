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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cur = a[0]
    best = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        if cur > best:
            best = cur

    if k % 2 == 0:
        print(best)
        return

    left_end = [0] * n
    cur = a[0]
    left_end[0] = cur
    for i in range(1, n):
        cur = max(a[i], cur + a[i])
        left_end[i] = cur

    right_start = [0] * n
    cur = a[-1]
    right_start[-1] = cur
    for i in range(n - 2, -1, -1):
        cur = max(a[i], cur + a[i])
        right_start[i] = cur

    ans = best
    for i in range(n):
        incl = left_end[i] + right_start[i] - a[i]
        cand = incl + b[i]
        if cand > ans:
            ans = cand

    print(ans)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
