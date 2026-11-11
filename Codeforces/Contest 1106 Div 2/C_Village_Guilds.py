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
    n = int(input())
    p = list(map(int, input().split()))

    par = [0] * (n + 1)
    for i in range(2, n + 1):
        par[i] = p[i - 2]

    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        depth[i] = depth[par[i]] + 1

    d = depth[:] 
    for i in range(n, 1, -1):
        pi = par[i]
        if d[i] > d[pi]:
            d[pi] = d[i]

    max1 = [-1] * (n + 1)
    max2 = [-1] * (n + 1)
    cnt  = [0] * (n + 1)

    for i in range(2, n + 1):
        pi = par[i]
        cnt[pi] += 1
        v = d[i]
        if v > max1[pi]:
            max2[pi] = max1[pi]
            max1[pi] = v
        elif v > max2[pi]:
            max2[pi] = v

    total = n
    for v in range(1, n + 1):
        if cnt[v] >= 2:
            total += max2[v] - depth[v]

    print(total)

t = int(input())
for _ in range(t):
    solve()