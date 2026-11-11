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
    ans = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += 1

    print(2 if ans == 2 else 1)

t = int(input())
for _ in range(t):
    solve()