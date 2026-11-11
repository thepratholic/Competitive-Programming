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
    a, b, c = sorted(list(map(int, input().split())))

    if a + b >= c:
        print(c - a)
        return

    else:
        while c > (a + b):
            c = a + b

        print(c - a)
        return
    

t = int(input())
for _ in range(t):
    solve()