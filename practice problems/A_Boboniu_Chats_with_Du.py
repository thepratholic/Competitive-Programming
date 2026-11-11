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
    n, d, m = map(int, input().split())
    a = list(map(int, input().split()))

    big = []
    small = []

    for x in a:
        if x > m:
            big.append(x)

        else:
            small.append(x)

    big.sort(reverse=True)
    small.sort(reverse=True)

    pre_big = [0]
    for x in big:
        pre_big.append(pre_big[-1] + x)

    pre_small = [0]
    for x in small:
        pre_small.append(pre_small[-1] + x)

    ans = 0
    for take_big in range(len(big) + 1):
        if take_big == 0:
            days = 0

        else:
            days = take_big + (take_big - 1) * d

        if days > n:
            break

        take_small = min(len(small), n - days)

        ans = max(ans, pre_big[take_big] + pre_small[take_small])

    print(ans)
    

# t = int(input())
# for _ in range(t):
solve()