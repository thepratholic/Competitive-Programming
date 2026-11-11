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
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    u = [0] * (n + 1)
    v = [0] * (n + 1)

    for i in range(1, n + 1):
        l[i], r[i], u[i], v[i] = map(int, input().split())

    ans = 0

    for m in range(n, 0, -1):
        dp = [0] + [n + 1] * m

        for i in range(1, n + 1):
            pos = bisect_left(dp, i)

            if pos == 0 or pos > m:
                continue

            if l[i] <= pos <= r[i]:
                continue

            ll = m - v[i] + 1
            rr = m - u[i] + 1

            if ll <= pos <= rr:
                continue

            dp[pos] = min(dp[pos], i)

        if dp[m] <= n:
            ans = m
            break

    print(ans)

t = int(input())
for _ in range(t):
    solve()