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
    s = input().strip()

    s = list(s)

    if n == 1:
        if s[0] == 'x':
            print(1)
            return

    ans = 0

    for i in range(n):
        if s[i] == 'x':

            if i == 0:
                if (i + 1) < n and s[i + 1] == 'x':
                    ans += 1

            elif i == n - 1:
                if (i - 1) >= 0 and s[i - 1] == 'x':
                    ans += 1

            else:
                if i - 1 >= 0 and s[i - 1] == 'x' and i + 1 < n and s[i + 1] == 'x':
                    ans += 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()