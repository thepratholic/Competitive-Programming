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
    p = list(map(int, input().split()))

    if n == 1:
        print(1)
        return

    print(*([2] * n))

t = int(input())
for _ in range(t):
    solve()