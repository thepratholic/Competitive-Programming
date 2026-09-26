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
    n, c = input().split()
    n = int(n)
    s = list(input().strip())

    l, r = 0, n - 1
    ans = 0

    while l < r:
        if s[l] != s[r]:
            if s[l] == c or s[r] == c:
                ans += 1
            else:
                ans += 2

        l += 1
        r -= 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()