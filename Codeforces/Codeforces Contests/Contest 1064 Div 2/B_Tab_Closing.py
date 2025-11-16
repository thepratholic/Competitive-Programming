import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    a, b, n = map(int, input().split())
    if a == b:
        print(1)
        return

    m = a // b
    g = gcd(a, b)
    A = a // g

    if n <= m:
        print(1)
    elif n == m + 1 and n % A == 0:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()