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

def query(x):
    print(x, flush=True)
    s = input().strip()
    return s

def solve():
    r = range(2, 101)

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 4, 9, 25, 49]
    cnt = 0


    for p in primes:
        ans = query(p)
        if ans == "yes":
            cnt += 1

    if cnt > 1:
        print("composite")
    else:
        print("prime")


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()