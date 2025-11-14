import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, a = map(int, input().split())
    v = list(map(int, input().split()))

    left = bisect_left(v, a)          
    right = n - bisect_right(v, a)

    if right >= left:
        print(a + 1)
        return
    else:
        print(a - 1)
        return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()