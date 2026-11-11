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
        self.par = list(range(n + 1))
        self.sz = [1] * (n + 1)

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.sz[a] < self.sz[b]:
            a, b = b, a

        self.par[b] = a
        self.sz[a] += self.sz[b]


def solve():
    n, x, y = map(int, input().split())
    p = [0] + list(map(int, input().split()))

    dsu = DSU(n)

    for i in range(1, n - x + 1):
        dsu.union(i, i + x)

    for i in range(1, n - y + 1):
        dsu.union(i, i + y)

    ok = True

    for i in range(1, n + 1):
        if dsu.find(i) != dsu.find(p[i]):
            ok = False
            break

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    solve()