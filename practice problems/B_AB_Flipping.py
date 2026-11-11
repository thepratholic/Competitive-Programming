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
    s = input().strip()

    ans = 0

    p = 0

    while p < n:
        if s[p] == 'B':
            p += 1
            continue
        
        x = 0

        while p < n and s[p] == 'A':
            x += 1
            p += 1

        gd = False

        while p < n and s[p] == 'B':
            x += 1
            p += 1
            gd = True

        if gd:
            ans += x

    ans -= 1 if ans else 0

    print(ans)

t = int(input())
for _ in range(t):
    solve()