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

    a = ""

    for i, c in enumerate(s):
        if c == '0':
            x = s[:i] + s[i + 1:]

            b = None

            for j, d in enumerate(x):
                if d == "1":
                    y = x[:j] + x[j + 1:]
                    if b is None or y < b:
                        b = y

            if a == "" or b > a:
                a = b

    print(a)

t = int(input())
for _ in range(t):
    solve()