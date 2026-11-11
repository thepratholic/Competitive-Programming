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
    b = list(map(int, input().split()))

    freq = Counter(b)

    u = sorted(freq.keys())
    c = [freq[x] for x in u]

    if u[0] != 0:
        print(-1)
        return

    k = len(u)
    v = [0] * k

    for j in range(k - 1):
        diff = u[j + 1] - u[j]

        if diff % c[j]:
            print(-1)
            return

        v[j] = diff // c[j]

        if j > 0 and v[j] <= v[j - 1]:
            print(-1)
            return

    if k == 1:
        v[0] = 1
    else:
        v[-1] = v[-2] + 1

    mp = {}
    for x, y in zip(u, v):
        mp[x] = y

    print(*[mp[x] for x in b])

t = int(input())
for _ in range(t):
    solve()