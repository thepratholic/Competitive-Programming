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

    s = input().strip()

    if n < 2 * k:
        print(-1)
        return
    
    cnt = 0

    for i in range(k):
        if s[i] == 'L':
            cnt += 1

    for i in range(n - k, n):
        if s[i] == 'R':
            cnt += 1

    print(cnt)

t = int(input())
for _ in range(t):
    solve()