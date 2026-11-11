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
def is_prime(x):
    if x < 2:
        return False

    if x % 2 == 0:
        return x == 2

    for d in range(3, isqrt(x) + 1, 2):
        if x % d == 0:
            return False

    return True

def solve():
    # Write your solution here
    n = int(input())

    print("YES" if is_prime(n + 1) else "NO")

t = int(input())
for _ in range(t):
    solve()