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
    n, m = map(int, input().split())

    g = [[[] for _ in range(2)] for _ in range(n)]
    deg = [[0] * 2 for _ in range(n)]

    for _ in range(m):
        t, u, v = map(int, input().split())
        t -= 1
        u -= 1
        v -= 1

        g[u][t].append(v)
        g[v][t].append(u)
        deg[u][t] += 1
        deg[v][t] += 1

    ans = [0] * n

    q = []

    for node in range(n):
        if deg[node][0] == 0 or deg[node][1] == 0:
            q.append(node)

    ptr = 0

    while ptr < len(q):
        cur = q[ptr]

        ptr += 1

        value = n - (ptr - 1)

        if deg[cur][0] == 0:
            value = -value

        ans[cur] = value

        for typ in range(2):
            for nxt in g[cur][typ]:

                if ans[nxt] != 0:
                    continue

                deg[nxt][typ] -= 1

                if deg[nxt][typ] == 0 and deg[nxt][typ ^ 1] != 0:
                    q.append(nxt)

    if len(q) != n:
        print("NO")
    
    else:
        print("YES")

        print(*ans)

t = int(input())
for _ in range(t):
    solve()