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

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != -1 and a[-1] != -1:
        ans = abs(a[-1] - a[0])
    else:
        ans = 0

    res = a[:]

    if res[0] == -1 and res[-1] == -1:
        res[0] = 0
        res[-1] = 0
    elif res[0] == -1:
        res[0] = res[-1]
    elif res[-1] == -1:
        res[-1] = res[0]

    for i in range(n):
        if res[i] == -1:
            res[i] = 0

    print(ans)
    print(*res)