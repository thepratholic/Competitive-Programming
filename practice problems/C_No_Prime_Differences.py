import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline



def solve():
    n, m = map(int, input().split())

    rows = list(range(1, n, 2)) + list(range(0, n, 2))

    for i in rows:
        row = [x for x in range(i * m + 1, (i + 1) * m + 1)]

        print(*row)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()