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
    n = int(input())

    a = [0] + list(map(int, input().split()))

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    par = [0] * (n + 1)
    ord = [1]

    for u in ord:
        for v in g[u]:
            if v != par[u]:
                par[v] = u
                ord.append(v)

    sub = [1] * (n + 1)

    for u in reversed(ord):
        if par[u]:
            sub[par[u]] += sub[u]

    ans = 0

    for v in range(1, n + 1):

        r = int(a[v] ** 0.5)
        if r * r != a[v]:
            continue

        one = two = three = 0

        for to in g[v]:

            if to == par[v]:
                size = n - sub[v]
            else:
                size = sub[to]

            three += two * size
            two += one * size
            one += size

        ans += two + three

    print(ans)

t = int(input())
for _ in range(t):
    solve()