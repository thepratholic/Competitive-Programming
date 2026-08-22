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
    a = list(map(int, input().split()))

    total = sum(a)

    ans = 10 ** 20
    pref = 0

    for i in range(n):
        pref += a[i]

        ans = min(ans, abs(pref - (total - pref)))

    print(ans)

# t = int(input())
# for _ in range(t):
solve()