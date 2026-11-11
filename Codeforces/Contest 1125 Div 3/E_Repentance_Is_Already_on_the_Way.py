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

    dp = [0] * n
    cur = 1 + (1 if a[-1] == b[-1] else 0)

    dp[-1] = cur

    for i in range(n - 2, -1, -1):
        cur += 1 + (1 if a[i] == b[i + 1] else 0)
        cur += 1 + (1 if b[i] == a[i + 1] else 0)

        dp[i] = max(cur, dp[i + 1] + 2 + (1 if a[i] == b[i] else 0) + (1 if b[i] == a[i + 1] else 0))

    print(dp[0])
 
t = int(input())
for _ in range(t):
    solve()