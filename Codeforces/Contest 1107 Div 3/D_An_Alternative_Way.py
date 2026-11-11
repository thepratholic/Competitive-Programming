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
    b = list(map(int, input().split()))

    sa = sb = 0
    ok = True
    for i in range(n):
        sa += a[i]
        sb += b[i]
        if sb < sa:
            ok = False

    print("YES" if ok else "NO")

t = int(input())
for _ in range(t):
    solve()