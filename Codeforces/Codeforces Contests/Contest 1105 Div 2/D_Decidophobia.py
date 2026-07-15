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
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    pref = [0] * (2 * n + 1)
    for i in range(2 * n):
        pref[i + 1] = pref[i] + a[i % n]

    ans = 0
    for i in range(n):

        if i >= d:
            s = pref[i + d + 1] - pref[i - d]

        else:
            s = pref[i + n + d + 1] - pref[i + n - d]

        nei = s - a[i]

        cont = 2 * d * a[i] - nei

        if cont > 0:
            ans += cont

    print(ans)

t = int(input())
for _ in range(t):
    solve()