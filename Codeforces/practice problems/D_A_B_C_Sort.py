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

    ans = []
    i = 0

    if n % 2:
        ans.append(a[0])
        i = 1

    while i < n:
        x, y = a[i], a[i + 1]
        if x > y:
            x, y = y, x
        ans.append(x)
        ans.append(y)
        i += 2

    print("YES" if ans == sorted(a) else "NO")


t = int(input())
for _ in range(t):
    solve()
