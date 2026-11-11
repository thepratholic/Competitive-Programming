# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple

import math
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
    a = list(map(int, input().split()))

    s, t = float('inf'), float('inf')
    ans = 0
    for i in range(n):
        if s > t:
            s, t = t, s

        if a[i] <= s: # first case
            s = a[i]

        elif a[i] <= t: # third case
            t = a[i]

        else: # second case
            s = a[i]
            ans += 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()