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
    w = list(map(int, input().split()))

    if n % 2 == 1:
        print("NO")
        return

    mn_odd = float('inf')
    mx_even = -float('inf')

    for i in range(n):
        if i % 2 == 0:    
            mn_odd = min(mn_odd, w[i])
        else:               
            mx_even = max(mx_even, w[i])

    if mx_even < mn_odd - 1:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()