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

class DSU:
    def __init__(self, n):
        self.sz = [1] * n
        self.parent = list(range(n))

    def find(self, x):
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.sz[pu] < self.sz[pv]:
            self.sz[pv] += self.sz[pu]
            self.parent[pu] = pv

        else:
            self.sz[pu] += self.sz[pv]
            self.parent[pv] = pu

        return True

    

def solve():
    # Write your solution here
    n = int(input())
    a = list(map(int, input().split()))

    mx = a[-1]

    pos = [-1] * (mx + 1)

    for i, v in enumerate(a):
        pos[v] = i

    dsu = DSU(n)

    ans = 0

    for g in range(mx, 0, -1):

        f = -1

        for mul in range(g, mx + 1, g):
            idx = pos[mul]

            if idx == -1:
                continue

            if f == -1:
                f = idx

            else:
                if dsu.union(f, idx):
                    ans += g

    print(ans)

# t = int(input())
# for _ in range(t):
solve()