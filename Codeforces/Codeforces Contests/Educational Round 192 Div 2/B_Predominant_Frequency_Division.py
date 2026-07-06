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
    a = list(map(int, input().split()))

    p = [0] * n
    q = [0] * n

    for i in range(n):
        if a[i] == 1:
            p[i] = 1
        else:
            p[i] = -1

        if a[i] == 3:
            q[i] = -1
        else:
            q[i] = 1

    for i in range(1, n):
        p[i] += p[i - 1]
        q[i] += q[i - 1]

    suf = [-float('inf')] * n
    suf[n - 2] = q[n - 2]

    for i in range(n - 3, 0, -1):
        suf[i] = max(suf[i + 1], q[i])

    ok = False

    for i in range(n - 2):
        if p[i] >= 0 and suf[i + 1] >= q[i]:
            ok = True
            break

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    solve()