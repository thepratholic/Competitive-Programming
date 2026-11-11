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
    s = input().strip()

    zero = s.count('0')

    if s[0] == '1':
        print(zero)
        return

    # ab s[0] is 0
    ans = n
    ones = 0

    for ch in s:
        if ch == '1':
            ones += 1

        else:
            zero -= 1

        ans = min(ans, ones + zero)

    print(ans)        

t = int(input())
for _ in range(t):
    solve()