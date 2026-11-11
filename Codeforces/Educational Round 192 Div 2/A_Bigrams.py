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
    k = int(input())

    c = list(map(int, input().split()))

    mx = max(c)
    cnt = sum(x >= 2 for x in c)

    if mx >= 3 or cnt >= 2:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()