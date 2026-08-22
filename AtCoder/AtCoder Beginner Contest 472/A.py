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

    ans = []

    for ch in s:
        if ch == 'A':
            ans.append(ch)

        else:
            ans.append(".")

    print("".join(ans))

# t = int(input())
# for _ in range(t):
solve()