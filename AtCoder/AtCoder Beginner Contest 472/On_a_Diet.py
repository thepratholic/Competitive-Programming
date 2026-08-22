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
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    total = 0
    q = deque()

    for i in range(n):
        while q and q[0][0] < i - m + 1:
            day, cal = q.popleft()
            total -= cal

        if total + a[i] <= k:
            print("Yes")
            q.append((i, a[i]))
            total += a[i]

        else:
            print("No")

    

# t = int(input())
# for _ in range(t):
solve()