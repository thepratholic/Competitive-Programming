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
    n, q_ = map(int, input().split())
    LOG = n.bit_length()

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)


    depth = [0] * (n + 1)
    up = [[0] * LOG for _ in range(n + 1)]

    q = deque()
    q.append(1)

    vis = [False] * (n + 1)
    vis[1] = True

    while q:
        node = q.popleft()

        for nei in g[node]:
            if not vis[nei]:
                depth[nei] = depth[node] + 1
                vis[nei] = True
                q.append(nei)
                up[nei][0] = node

    # pre-processing of up table
    for k in range(1, LOG):
        for node in range(1, n + 1):
            up[node][k] = up[up[node][k - 1]][k - 1]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u

        diff = depth[u] - depth[v]

        k = 0
        while diff:
            if diff & 1:
                u = up[u][k]

            diff >>= 1
            k += 1

        if u == v:
            return u
        
        for k in range(LOG - 1, -1, -1):
            if up[u][k] != up[v][k]:
                u = up[u][k]
                v = up[v][k]

        return up[u][0]
    
    for _ in range(q_):
        u, v = map(int, input().split())
        print(depth[u] + depth[v] - (2 * depth[lca(u, v)]))
    

solve()