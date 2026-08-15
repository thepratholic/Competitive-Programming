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

    neg = sorted(x for x in a if x < 0)
    pos = sorted(x for x in a if x > 0)

    i = 0
    j = len(neg) - 1

    ans = 0
    cur = 0

    while i < len(pos) or j >= 0:
        if j < 0:
            nxt = pos[i]
            i += 1

        elif i == len(pos):
            nxt = neg[j]
            j -= 1

        else:
            d_pos = abs(cur - pos[i])
            d_neg = abs(cur - neg[j])

            if d_neg <= d_pos:
                nxt = neg[j]
                j -= 1

            else:
                nxt = pos[i]
                i += 1

        ans += abs(cur - nxt)
        cur = nxt

    print(ans)

# t = int(input())
# for _ in range(t):
solve()