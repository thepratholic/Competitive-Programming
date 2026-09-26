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

    b = []

    for x in a:
        if not b or b[-1][0] != x:
            b.append([x, 1])
        else:
            b[-1][1] += 1

    m = len(b)

    for i in range(m - 1):
        if b[i][1] >= 2 and b[i + 1][1] >= 2:
            print(m + 2)
            return

    for i in range(m):
        if b[i][1] < 2:
            continue

        if i > 0:
            if i == 1 or b[i - 2][0] != b[i][0]:
                print(m + 1)
                return

        if i < m - 1:
            if i == m - 2 or b[i + 2][0] != b[i][0]:
                print(m + 1)
                return

    print(m)

t = int(input())
for _ in range(t):
    solve()