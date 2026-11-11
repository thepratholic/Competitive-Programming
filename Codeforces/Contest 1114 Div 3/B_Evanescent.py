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
    s = input().strip()

    r = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            r += 1

    ans = 10 ** 9

    for i in range(1, n - 1):
        d = 0

        if s[i - 1] != s[i]:
            d -= 1

        if s[i] != s[i + 1]:
            d -= 1

        if s[i - 1] != s[i + 1]:
            d += 1

        ans = min(ans, r + d)

    print(ans)


t = int(input())
for _ in range(t):
    solve()