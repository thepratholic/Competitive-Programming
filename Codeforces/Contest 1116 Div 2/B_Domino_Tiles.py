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
MOD = 998244353

def f(s, st):
    a = b = True

    for j, i in enumerate(range(st, len(s), 2)):
        if s[i] == '?':
            continue

        x = int(s[i])

        if x != j % 2:
            a = False

        if x != 1 - j % 2:
            b = False

    return a + b

def solve():
    # Write your solution here
    n = int(input())
    s = input().strip()

    print(f(s, 0) * f(s, 1) % MOD)

t = int(input())
for _ in range(t):
    solve()