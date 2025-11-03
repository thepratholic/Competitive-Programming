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

    grid = [[0] * n for _ in range(n)]

    for i in range(n):
        grid[i][0] = i

    for j in range(n):
        grid[0][j] = j

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            else:
                grid[i][j] = i ^ j


    for row in grid:
        print(*row)

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()