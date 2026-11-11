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
from heapq import merge

input = stdin.readline

def solve():
    n, m = map(int, input().split())

    v = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = m
    t = []

    for i in range(n - 1, -1, -1):
        if ans == 1:
            break

        row = sorted(a[i], reverse=True)

        u = list(merge(t, row, reverse=True))

        s = 0
        for j, x in enumerate(u):
            s += x
            if s >= v[i]:
                ans = min(ans, j + 1)
                break

        t = u[ : m - 1]

    print(ans)


t = int(input())
for _ in range(t):
    solve()