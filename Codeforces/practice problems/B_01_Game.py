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
    odd = even = 0

    for ch in s:
        if ch == '1':
            odd += 1

        else:
            even += 1

    mn = min(even, odd)

    if mn & 1:
        print("DA")

    else:
        print("NET")

t = int(input())
for _ in range(t):
    solve()