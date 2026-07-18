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
    a = input().split()
    b = input().split()

    d1 = d0 = u1 = u0 = 0

    for ai, bi in zip(a, b):
        if ai == bi:
            if ai == '1':
                u1 += 1
            else:
                u0 += 1
        else:
            if ai == '1':
                d1 += 1
            else:
                d0 += 1

    s = d1 + d0

    if s == 0:
        print(0)
    elif d1 & 1:
        print(1)
    elif d1 > 0:
        print(2)
    else:
        if u1 >= 1 and u0 >= 1:
            print(2)
        else:
            print(-1)

t = int(input())
for _ in range(t):
    solve()