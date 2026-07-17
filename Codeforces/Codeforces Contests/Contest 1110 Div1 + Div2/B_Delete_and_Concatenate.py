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
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    base = sum(a) - n * c
    m = n // 2

    best = 0
    pref = 0
    for i in range(m):
        pref += a[i]
        gain = (i + 1) * c - pref
        
        if gain > best:
            best = gain
 
        elif (i+1)*c - pref < gain and a[i] > c:
            pass

    print(base + best)

t = int(input())
for _ in range(t):
    solve()