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

    freq = [0] * (m + 1)

    for x in a:
        freq[x] += 1

    suffix = [0] * (m + 2)

    for x in range(m, 0, -1):
        suffix[x] = suffix[x + 1] + freq[x]

    ans = 0

    for x in range(1, m + 1):

        cur = suffix[x]

        if 2 * x <= m:
            cur += freq[2 * x]

        ans = max(ans, cur)

    print(ans)

t = int(input())
for _ in range(t):
    solve()