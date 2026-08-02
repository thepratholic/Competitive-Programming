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
    n, q = map(int, input().split())

    s = " " + input().strip()
    t = " " + input().strip()

    p01 = [0] * (n + 1)
    p10 = [0] * (n + 1)

    for i in range(1, n + 1):
        p01[i] = p01[i - 1] + (s[i] == '0' and t[i] == '1')
        p10[i] = p10[i - 1] + (s[i] == '1' and t[i] == '0')


    for _ in range(q):
        l, r = map(int, input().split())

        x = p01[r] - p01[l - 1]
        y = p10[r] - p10[l - 1]

        if 2 * max(x, y) <= (r - l + 1):
            print("YES")
        else:
            print("NO")


t = int(input())
for _ in range(t):
    solve()