import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    a = list(map(int, input().split()))
    pref = 0
    best_min = 0 
    max_delta = 0
    for r in range(1, n + 1):
        pref += a[r - 1]

        F = r * r + r - pref

        delta = F - best_min
        if delta > max_delta:
            max_delta = delta

        if F < best_min:
            best_min = F

            
    print(pref + max_delta)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
