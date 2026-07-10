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
    n, q = map(int, input().split())
    LOG = max(1, n.bit_length())
    a = list(map(int, input().split()))

    parent = [0] * (n + 1)
    for node in range(2, n + 1):
        parent[node] = a[node - 2]

    depth = [0] * (n + 1)
    for node in range(2, n + 1):
        depth[node] = depth[parent[node]] + 1

    up = [[0] * LOG for _ in range(n + 1)]
    for node in range(1, n + 1):
        up[node][0] = parent[node] # for only 2^0th ancestor

    # pre-processing karo
    for k in range(1, LOG):
        for node in range(1, n + 1):
            p = up[node][k - 1]
            up[node][k] = up[p][k - 1]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u

        diff = depth[u] - depth[v]
        k = 0

        while diff > 0:
            if diff & 1:
                u = up[u][k]

            diff >>= 1
            k += 1

        if u == v:
            return u
        
        # edge case nai hai, so ab hum vertical binary search karenge
        for k in range(LOG - 1, -1, -1):
            if up[u][k] != up[v][k]:
                u = up[u][k]
                v = up[v][k]

        return up[u][0]
    
    out = []
    for _ in range(q):
        u, v = map(int, input().split())
        out.append(str(lca(u, v)))

    stdout.write("\n".join(out) + "\n")

solve()