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

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * (n + 1)
    color = [-1] * (n + 1)

    q = deque([1])
    color[1] = 0

    while q:
        node = q.popleft()

        for v in adj[node]:
            if color[v] == -1:
                color[v] = color[node] ^ 1
                parent[v] = node
                q.append(v)

            elif color[node] == color[v]: # odd length cycle mil gayi!!
                pu = []
                x = node
                while x != -1:
                    pu.append(x)
                    x = parent[x]

                pv = []
                x = v
                while x != -1:
                    pv.append(x)
                    x = parent[x]

                i = len(pu) - 1
                j = len(pv) - 1

                while pu[i] == pv[j]:
                    i -= 1
                    j -= 1

                cycle = pu[ : i + 1]
                cycle.append(pu[i + 1])
                cycle += pv[j :: -1]

                print(len(cycle))
                print(*cycle)

                return

    print(-1)

t = int(input())
for _ in range(t):
    solve()