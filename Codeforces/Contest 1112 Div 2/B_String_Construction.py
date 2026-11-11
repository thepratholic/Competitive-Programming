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

    runs = n - k

    if runs == 1:
        print(-1)
        return

    lens = [1] * runs

    extra = k       

    lens[0] += extra // 2
    lens[1] += extra - extra // 2

    ans = []
    ch = '0'

    for x in lens:
        ans.append(ch * x)
        ch = '1' if ch == '0' else '0'

    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()