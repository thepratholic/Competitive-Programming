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
    ans = [0] * n

    even = 2
    odd = 1

    for i in range(n):
        if (i + 1) % 2 == 1:     
            ans[i] = even
            even += 2
        else:                 
            ans[i] = odd
            odd += 2

    print(*ans)

t = int(input())
for _ in range(t):
    solve()