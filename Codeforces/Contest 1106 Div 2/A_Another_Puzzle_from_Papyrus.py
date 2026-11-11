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
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans1 = 0
    ok = True
    for x, y in zip(a, b):
        if x < y:
            ok = False
            break
        ans1 += x - y

    sa = sorted(a)
    sb = sorted(b)

    ans2 = 0
    possible = True

    for x in reversed(sb):
        idx = bisect_left(sa, x)

        if idx == len(sa):
            possible = False
            break

        ans2 += sa[idx] - x
        sa.pop(idx)

    INF = 10 ** 18
    if not ok:
        ans1 = INF
    if not possible:
        ans2 = INF

    ans = min(ans1, ans2 + c)

    if ans == INF:
        print(-1)
    else:
        print(ans)

t = int(input())
for _ in range(t):
    solve()