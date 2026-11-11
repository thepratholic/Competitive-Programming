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
    n, k, m = map(int, input().split())
    res = []

    if k > m:
        print("NO")
        return
    
    print("YES")
    res = [0] * n
    p_prev = 0

    for i in range(1, n+1):
        p_cur = i % k
        diff = (p_cur - p_prev) % m
        if diff == 0:
            diff = m
        res[i-1] = diff
        p_prev = p_cur

    print(*res)

t = int(input())
for _ in range(t):
    solve()