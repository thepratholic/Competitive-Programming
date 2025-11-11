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
    a = list(map(int, input().split()))

    mpp = defaultdict(lambda : [0, 0]) # even, odd

    for i, val in enumerate(a):
        mpp[val][i % 2] += 1

    a.sort()

    for i, val in enumerate(a):
        mpp[val][i % 2] -= 1

    for k, v in mpp.items():
        if v[0] != 0 or v[1] != 0:
            print("NO")
            return
        
    print("YES")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()