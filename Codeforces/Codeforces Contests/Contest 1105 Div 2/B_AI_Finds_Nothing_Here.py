import sys
import os
from sys import stdin, stdout
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
MOD = 998244353

def solve():
    n, m, r, c = map(int, input().split())

    exp = n * m - (n - r + 1) * (m - c + 1)
    print(pow(2, exp, MOD))

t = int(input())
for _ in range(t):
    solve()