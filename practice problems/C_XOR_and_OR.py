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
    a = input().strip()
    b = input().strip()

    c1, c2 = a.count('1'), b.count('1')

    if ((c1 != 0 and c2 != 0) or (c1 == c2)) and len(a) == len(b):
        print("YES")

    else:
        print("NO")


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve() 