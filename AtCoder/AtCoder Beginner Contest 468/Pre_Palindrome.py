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
    s = input().strip()
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    ans = n

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1

            if length == 2:
                dp[l][r] = 0 if s[l] == s[r] else 1
            else:
                dp[l][r] = dp[l + 1][r - 1]
                if s[l] != s[r]:
                    dp[l][r] += 1

            if dp[l][r] <= 1:
                ans += 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()