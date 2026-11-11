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
    a = map(int, input().split())

    tot = 2 * n
    f = [-1] * (n + 1)
    s = [-1] * (n + 1)

    for i, x in enumerate(a):
        if f[x] == -1:
            f[x] = i
        else:
            s[x] = i

    iv = []
    for x in range(1, n + 1):
        iv.append((s[x], f[x]))

    iv.sort()

    rs = [x[0] for x in iv]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        r, l = iv[i - 1]

        ln = r - l + 1
        w = ln * (ln - 1)

        p = bisect_left(rs, l, 0, i - 1)

        dp[i] = max(dp[i - 1], dp[p] + w)

    print(tot + dp[n])

t = int(input())
for _ in range(t):
    solve()