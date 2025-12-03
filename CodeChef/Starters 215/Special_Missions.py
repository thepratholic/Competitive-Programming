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
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    if '0' not in s:
        print(0)
        return
    
    ans = 0
    normal, spe = 0, 0

    for i in range(n):
        if s[i] == '0':
            normal += a[i]

        else:
            spe += a[i]

    if normal < c:
        print(normal)
        return
    else:
        profit = spe - c

        if profit > 0:
            print(profit + normal)

        else:
            print(normal)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()