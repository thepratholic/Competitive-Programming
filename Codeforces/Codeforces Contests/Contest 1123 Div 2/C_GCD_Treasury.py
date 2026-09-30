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
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    div = []
    d = 1

    while d * d <= x:
        if x % d == 0:
            if d > 1:
                div.append(d)

            other = x // d
            if other != d and other > 1:
                div.append(other)

        d += 1

    best = 0

    for d in div:
        cur = 0

        for v in a:
            if v % d == 0:
                cur += v

        best = max(best, cur)

    print(best)

t = int(input())
for _ in range(t):
    solve()