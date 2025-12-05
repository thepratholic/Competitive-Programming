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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_k = 0
    min_k = 0

    for i in range(n):
        val_a = a[i]
        val_b = b[i]

        cand1 = max_k - val_a
        cand2 = val_b - min_k
        cand3 = min_k - val_a
        cand4 = val_b - max_k

        max_k = max(cand1, cand2)
        min_k = min(cand3, cand4)

    print(max_k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()