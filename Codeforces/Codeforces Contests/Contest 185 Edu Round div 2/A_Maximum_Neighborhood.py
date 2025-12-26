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
    
    if n == 1:
        print(1)
    elif n == 2:
        print(9)
    elif n == 3:
        print(29)
    elif n == 4:
        print(56)
    else:
        print(5 * (n * n - n - 1))



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()