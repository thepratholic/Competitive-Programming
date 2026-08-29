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
    n, k = map(int, input().split())

    cur = [0] * n
    ans = []

    def f(idx, rem):
        if idx == n - 1:
            coef = idx + 1

            if rem % coef == 0:
                cur[idx] = rem // coef
                ans.append(" ".join(map(str, cur)))

            return

        coef = idx + 1

        mx = rem // coef

        for x in range(mx + 1):
            cur[idx] = x

            new_rem = rem - (coef * x)

            f(idx + 1, new_rem)

    f(0, k)

    sys.stdout.write("\n".join(ans))

# t = int(input())
# for _ in range(t):
solve()