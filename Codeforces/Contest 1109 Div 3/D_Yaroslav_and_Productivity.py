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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    pref = [0] * (n + 1)

    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]

    ans = 0
    prev = 0

    for pos in b:
        s = pref[pos] - pref[prev]

        ans += abs(s)

        prev = pos

    ans += pref[n] - pref[prev]
    print(ans)

t = int(input())
for _ in range(t):
    solve()