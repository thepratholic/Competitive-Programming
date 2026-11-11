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
    a = list(map(int, input().split()))

    ans = 0
    while len(set(a)) == 3:
        mx = a.index(max(a))
        mn = a.index(min(a))
        a[mx] -= 1
        a[mn] += 1
        ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()