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
    x, y = map(int, input().split())

    vika = (x + y) % 2

    can = True

    for _ in range(k):
        a, b = map(int, input().split())

        if (a + b) % 2 == vika:
            can = False

    print("NO" if not can else "YES")

t = int(input())
for _ in range(t):
    solve()