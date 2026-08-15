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

    d = defaultdict(int)

    for _ in range(n):
        s = input().strip().lower()
        d[s] += 1

    print(max(d.values()))

# t = int(input())
# for _ in range(t):
solve()