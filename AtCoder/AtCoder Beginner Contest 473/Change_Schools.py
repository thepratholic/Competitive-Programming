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

    f = [0] * k

    for x in a:
        f[x - 1] += 1

    mx = max(f)

    ans = 0

    for cnt in f:
        if cnt + 1 >= mx:
            ans += 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()