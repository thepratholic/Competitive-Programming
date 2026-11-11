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
    s = input().strip()
    t = input().strip()

    n, m = len(s), len(t)

    if m > n:
        print("NO")
        return
    
    i, j = n - 1, m - 1

    while i >= 0 and j >= 0:
        if s[i] == t[j]:
            i -= 1
            j -= 1

        else:
            i -= 2

    print("YES" if j == -1 else "NO")


t = int(input())
for _ in range(t):
    solve()