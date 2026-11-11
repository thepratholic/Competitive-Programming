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

    pr = 0
    ok = True

    for k in range(1, n + 1):
        pr += a[k - 1]
        t = k * (k + 1) // 2
        if pr < t:
            ok = False
            break

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    solve()