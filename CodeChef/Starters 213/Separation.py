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
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for i, val in enumerate(a):
        if val == x:
            print("YES")
            return
        
    a.sort()

    for i in range(n - 1):
        if a[i] < x and a[i + 1] > x or a[i + 1] < x and a[i] > x:
            print("NO")
            return
        
    print("YES")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()