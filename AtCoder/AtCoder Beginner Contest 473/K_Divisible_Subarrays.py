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
    a = list(map(int, input().split()))

    best = {0 : 0}
    pref = 0
    prev_dp = 0

    for x in a:
        pref += x
        pref %= k

        cur_dp = prev_dp

        if pref in best:
            cur_dp = max(cur_dp, best[pref] + 1)

        if pref not in best:
            best[pref] = cur_dp

        else:
            best[pref] = max(best[pref], cur_dp)

        prev_dp = cur_dp

    print(prev_dp)

# t = int(input())
# for _ in range(t):
solve()