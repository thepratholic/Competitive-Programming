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
    s = input().strip()

    if "2026" in s:
        print(0)
        return
    
    if "2026" not in s and "2025" in s:
        print(1)
        return
    
    else:
        print(0)
        return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()