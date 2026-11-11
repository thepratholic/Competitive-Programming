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

    a = list(map(int, input().split()))

    d = Counter(a)

    sm = sum(a)

    mx = a[0]
    f = 0

    for x, c in d.items():
        if c > f:
            f = c
            mx = x

    r = n - f

    if f <= r + 2:
        print(sm)
        return

    s = 0
    for x in a:
        if x != mx:
            s += x

    print(s + (r + 2) * mx)

t = int(input())
for _ in range(t):
    solve()