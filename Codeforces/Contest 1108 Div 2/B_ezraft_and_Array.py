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

    if n == 1:
        print(1)
        return
    
    if n == 2:
        print(-1)
        return
    
    ans = [1, 2, 3]
    for i in range(n - 3):
        ans.append(2 * ans[-1])

    print(*ans)

t = int(input())
for _ in range(t):
    solve()