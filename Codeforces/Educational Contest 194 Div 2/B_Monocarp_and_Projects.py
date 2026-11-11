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
    x, y, k = map(int, input().split())

    d = y - x

    if d == 0:
        print(0)
        return

    lo, hi = 0, k

    while lo < hi:
        mid = (lo + hi) // 2

        if x + mid > d:
            hi = mid
        else:
            lo = mid + 1

    p = lo

    ans = 0

    for i in range(p):
        ans += d % (x + i)

    ans += (k - p) * d

    print(ans)

t = int(input())
for _ in range(t):
    solve()