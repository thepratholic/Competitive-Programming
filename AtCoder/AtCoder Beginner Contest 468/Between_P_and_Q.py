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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    @lru_cache(None)
    def f(mask, gp, lq):
        pos = mask.bit_count()

        if pos == n:
            return int(gp and lq)

        ans = 0

        for x in range(1, n + 1):

            if mask & (1 << (x - 1)):
                continue

            if not gp:
                if x < a[pos]:
                    continue
                ngp = gp or (x > a[pos])

            else:
                ngp = True

            if not lq:
                if x > b[pos]:
                    continue
                nlq = lq or (x < b[pos])

            else:
                nlq = True

            ans += f(mask | (1 << (x - 1)), ngp, nlq)

        return ans

    print(f(0, False, False))

# t = int(input())
# for _ in range(t):
solve()