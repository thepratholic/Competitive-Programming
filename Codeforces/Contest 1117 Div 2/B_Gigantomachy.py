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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = a[0] + n - 1
    y = b[0] + m - 1

    if x < y:
        print(2)
    else:
        print(1)

t = int(input())
for _ in range(t):
    solve()