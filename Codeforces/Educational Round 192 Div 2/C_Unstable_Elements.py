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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sl = [0] * (n + 1)
    cl = [0] * (n + 1)

    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        sz = j - i
        sl[sz] += sz
        cl[sz] += 1
        i = j

    ans = 0
    rs = 0
    rc = 0

    for v in range(n, 0, -1):
        if cl[v]:
            rs += sl[v]
            rc += cl[v]

            num = k - rs
            if num % rc == 0:
                e = num // rc
                if e + v >= 1:
                    ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()