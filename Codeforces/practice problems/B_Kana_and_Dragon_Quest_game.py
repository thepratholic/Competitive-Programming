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
    h, n, m = map(int, input().split())

    minus = m * 10

    if minus >= h:
        print("YES")
        return

    while h > 0 and n > 0 and ((h // 2) + 10) < h:
        n -= 1
        h >>= 1
        h += 10

    if minus >= h:
        print("YES")

    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()