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

input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    flip = 0
    ans = []

    for i in range(n - 1, -1, -1):

        cur = a[i]
        if flip:
            cur = -cur

        if cur > 0:
            ans.append(i + 1)
            flip ^= 1

    print(len(ans))
    print(*ans)


t = int(input())
for _ in range(t):
    solve()