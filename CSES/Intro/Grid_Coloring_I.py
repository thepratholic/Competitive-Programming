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
    n, m = map(int, input().split())

    g = []

    for _ in range(n):
        g.append(list(input().strip()))

    def isValid(i, j):
        return i >= 0 and i < n and j >= 0 and j < m

    # ans alwasy exists
    for i in range(n):
        for j in range(m):
            avoid = {g[i][j]}

            if isValid(i - 1, j):
                avoid.add(g[i - 1][j])
            
            if isValid(i, j - 1):
                avoid.add(g[i][j - 1])

            for ch in ['A', 'B', 'C', 'D']:
                if ch not in avoid:
                    g[i][j] = ch
                    break

    for row in g:
        for i in range(len(row)):
            print(row[i], end="")

        print()
            

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()