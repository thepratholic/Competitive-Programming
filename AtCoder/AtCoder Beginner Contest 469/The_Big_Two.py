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
    n, m = map(int, input().split())

    a = [0] * m
    b = [0] * m

    for i in range(m):
        a[i], b[i] = map(int, input().split())

    def miss(x):
        for i in range(m):
            if a[i] != x and b[i] != x:
                return i
        return -1

    def cnt(x):
        i = miss(x)

        if i == -1:
            return n - 1

        res = 0
        for y in (a[i], b[i]):
            ok = True

            for j in range(m):
                if a[j] != x and b[j] != x and a[j] != y and b[j] != y:
                    ok = False
                    break

            if ok:
                res += 1

        return res

    def chk(x, y):
        for i in range(m):
            if a[i] != x and b[i] != x and a[i] != y and b[i] != y:
                return False
        return True

    x, y = a[0], b[0]

    ans = cnt(x) + cnt(y)

    if chk(x, y):
        ans -= 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()