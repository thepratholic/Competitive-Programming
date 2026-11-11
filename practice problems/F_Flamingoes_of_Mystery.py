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

def query(l, r):
    print("? ", l, r, flush=True)
    x = int(input())
    return x

def solve():
    n = int(input())

    sum1to3 = query(1, 3)
    sum1to2 = query(1, 2)
    sum2to3 = query(2, 3)

    ans = [0] * (n + 1)
    ans[1] = sum1to3 - sum2to3
    ans[2] = sum1to2 - ans[1]
    ans[3] = sum2to3 - ans[2]

    for i in range(4, n + 1):
        x = query(i - 1, i)
        ans[i] = x - ans[i - 1]

    ans = ans[1:]
    print("! ", *ans, flush=True)
    

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()