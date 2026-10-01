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
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    is_sorted = True

    for i in range(n - 1):
        if p[i] > p[i + 1]:
            is_sorted = False
            break

    if is_sorted:
        print(0)
        return

    if k == n:
        print(1)
        return

    v = 0
    need = 1

    for i in range(n):
        if p[i] == need:
            need += 1
            v += 1

    print(ceil((n - v) / k))

    

t = int(input())
for _ in range(t):
    solve()