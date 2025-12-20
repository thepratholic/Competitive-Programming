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

def check(k):
    m = 1 # no of digits in the group like 1d, 2d, 3d
    count = 9 # numbers in the current group i.e 9 in 1st grp, 90 in 2nd grp etc
    start = 1 # group starts from 1

    while k > m * count:
        k -= m * count
        m += 1
        count *= 10
        start *= 10

    
    # specific kth in the group
    num = start + (k - 1) // m
    pos = (k - 1) % m

    return str(num)[pos]


def solve():
    q = int(input())

    for _ in range(q):
        k = int(input())

        print(check(k))

    

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()