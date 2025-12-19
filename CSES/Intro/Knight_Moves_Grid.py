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
    n = int(input())

    g = [[-1] * n for _ in range(n)]
    g[0][0] = 0

    q = deque()
    q.append((0, 0))


    def isValid(i, j):
        return 0 <= i < n and 0 <= j < n
    
    offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    while q:
        u, v = q.popleft()

        for x, y in offsets:
            nRow, nCol = u + x, v + y

            if isValid(nRow, nCol) and g[nRow][nCol] == -1:
                q.append((nRow, nCol))
                g[nRow][nCol] = g[u][v] + 1

    
    for row in g:
        print(*row)


if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()