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
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    apart = []

    for i in range(n):
        ok = True
        for j in range(n):

            if j != i and abs(a[i] - a[j]) < d:
                ok = False
                break

        if ok:
            apart.append(i + 1)

    print(len(apart))
    print(*apart)

# t = int(input())
# for _ in range(t):
solve()