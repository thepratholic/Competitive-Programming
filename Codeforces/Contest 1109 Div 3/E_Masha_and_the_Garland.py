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
    n, q = map(int, input().split())
    s = input().strip()

    pref = [0] * n
    for i in range(1, n):
        bad = 1 if s[i] == s[i - 1] else 0
        pref[i] = pref[i - 1] + bad

    for _ in range(q):
        l, r, k = map(int, input().split())

        if l == r:
            print("YES")
            continue

        c = pref[r - 1] - pref[l - 1]

        if 2 * k >= c:
            print("YES")

        else:
            print("NO")

t = int(input())
for _ in range(t):
    solve()