import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    

    want = set(range(1, k + 1))
    h = sum(1 for x in a[:k] if x in want)

    print(k - h)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()