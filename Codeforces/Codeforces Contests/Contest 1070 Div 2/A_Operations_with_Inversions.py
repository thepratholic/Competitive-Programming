# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right, insort
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pref = []
    ans = 0

    for j in range(n):
        x = a[j]

        pos = bisect_right(pref, x)

        if pos < len(pref):
            ans += 1

        insort(pref, x) 

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()