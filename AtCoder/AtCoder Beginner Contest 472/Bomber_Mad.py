import sys
import os
from sys import stdin, stdout
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *
from string import *
from decimal import *
from fractions import Fraction
import re

input = stdin.readline

def solve():
    # Write your solution here
    h, w, k = map(int, input().split())
    s = [input().strip() for _ in range(h)]

    row_bomb = [False] * h
    col_bomb = [False] * w

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                row_bomb[i] = True
                col_bomb[j] = True

    q = deque()
    dist = [-1] * (h * w)

    for i in range(h):
        for j in range(w):
            if s[i][j] == '.' and not row_bomb[i] and not col_bomb[j]:
                idx = i * w + j
                q.append(idx)
                dist[idx] = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def valid(i, j):
        return i >= 0 and i < h and j >= 0 and j < w

    ans = 0

    while q:
        idx = q.popleft()

        d = dist[idx]

        if d > k:
            continue

        ans += 1

        r = idx // w
        c = idx % w

        for dx, dy in dirs:
            nr = dx + r
            nc = dy + c

            if valid(nr, nc) and s[nr][nc] == '.':
                nidx = nr * w + nc

                if dist[nidx] != -1:
                    continue

                dist[nidx] = d + 1
                if dist[nidx] <= k:
                    q.append(nidx)

    print(ans)

# t = int(input())
# for _ in range(t):
solve() 