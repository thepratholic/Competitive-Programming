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
    b = list(map(int, input().split()))

    sa = 0
    for x in a:
        sa ^= x

    sb = 0
    for x in b:
        sb ^= x

    da = [x ^ sa for x in a]
    da.append(sa)

    db = [x ^ sb for x in b]
    db.append(sb)

    da.sort()
    db.sort()

    if da == db:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()