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

    freq = defaultdict(int)
    ans = 0

    for _ in range(n):
        x, y = map(int, input().split())
        freq[x] += y
        ans = max(ans, x)

    def check(t):
        extra = freq[0]
        req = 1

        for i in range(t - 1, 0, -1):
            c = freq[i]

            if c >= req:
                extra += (c - req)

            else:
                deficit = req - c
                req += deficit

                if req >= 10 ** 15:
                    return False

        return req <= extra


    while check(ans + 1):
        ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()