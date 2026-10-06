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

    pref = [0] * n
    for i in range(1, n):
        pref[i] = pref[i - 1] + max(0, a[i - 1] - a[i])

    ans = []

    for _ in range(m):
        s, t = map(int, input().split())

        s -= 1
        t -= 1

        if s < t:
            ans.append(pref[t] - pref[s])

        else:
            ans.append((a[s] + pref[s]) - (a[t] + pref[t]))

    for x in ans:
        print(x)



# t = int(input())
# for _ in range(t):
solve()