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
    s, t = input().split()

    need = Counter(t)
    ans = []

    for ch in reversed(s):
        if need[ch] > 0:
            ans.append(ch)
            need[ch] -= 1

    ans.reverse()

    print("YES" if "".join(ans) == t else "NO")

t = int(input())
for _ in range(t):
    solve()