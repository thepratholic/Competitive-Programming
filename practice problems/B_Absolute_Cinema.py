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

    s = 0

    for i in range(n):
        if a[i] < b[i]:
            s += b[i]

        else:
            s += a[i]

    ans = 0

    for i in range(n):
        ans = max(ans, s + min(a[i], b[i]))

    print(ans)
    

t = int(input())
for _ in range(t):
    solve()