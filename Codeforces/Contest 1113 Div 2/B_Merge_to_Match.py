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
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < 2 * m:
        print("NO")
        return

    a.sort()
    b.sort()

    for i in range(m):
        if not (a[i] < b[i] < a[n - m + i]):
            print("NO")
            return

    print("YES")

t = int(input())
for _ in range(t):
    solve()