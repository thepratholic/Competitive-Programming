import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    b, c, d = map(int, input().split())

    a = b ^ d

    if (a | b) - (a & c) == d:
        print(a)

    else:
        print(-1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()