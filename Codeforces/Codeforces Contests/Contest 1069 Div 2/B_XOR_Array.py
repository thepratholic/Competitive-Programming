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
    n, l, r = map(int, input().split())

    p_prev = 0
    for i in range(1, n + 1):
        if i == r:
            p_i = l - 1
        else:
            p_i = i

        ai = p_prev ^ p_i
        print(ai, end=" ")

        p_prev = p_i

    print()

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()