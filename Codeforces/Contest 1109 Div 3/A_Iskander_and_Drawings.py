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

    mx = 0

    s = input().strip()

    for i in range(n):
        if s[i] == '#':
            cur = 0

            j = i

            while j < n and s[j] == '#':
                j += 1

            sz = j - i

            mx = max(mx, sz)

    if mx == 0:
        print(0)
        
    else:
        print((mx // 2) + 1 if mx & 1 else mx // 2)

t = int(input())
for _ in range(t):
    solve()