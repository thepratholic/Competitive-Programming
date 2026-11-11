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
    n, p, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + a[i - 1]

        if i >= k:
            dp[i] = min(dp[i], dp[i - k] + a[i - 1])

    for ans in range(n, -1, -1):
        if dp[ans] <= p:
            print(ans)
            return
        
    print(0)

t = int(input())
for _ in range(t):
    solve()