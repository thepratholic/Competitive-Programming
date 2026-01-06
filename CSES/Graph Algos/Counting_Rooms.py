# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys
sys.setrecursionlimit(10**7)

from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = []
    vis = [[False] * m for _ in range(n)]

    for _ in range(n):
        row = list(input().strip())
        graph.append(row)

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def isValid(i, j):
        return 0 <= i < n and 0 <= j < m

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        vis[x][y] = True

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in dirs:
                nRow, nCol = dx + cur_x, dy + cur_y
                if isValid(nRow, nCol) and graph[nRow][nCol] == '.' and not vis[nRow][nCol]:
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))

        
    
    rooms = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.' and not vis[i][j]:
                bfs(i, j)
                rooms += 1

    print(rooms)

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()