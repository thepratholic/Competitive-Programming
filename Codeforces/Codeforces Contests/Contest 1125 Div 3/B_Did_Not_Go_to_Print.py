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

    stack = []
    seen = set()

    for i, c in enumerate(s, 1):

        if c == '1':
            stack.append(i)

        elif c == '2':
            if stack:
                doc = stack.pop()
                seen.add(doc)
            else:
                seen.add(i)

        else:  
            seen.add(i)

    ans = []

    for i in range(1, n + 1):
        if i not in seen:
            ans.append(i)

    print(len(ans))
    print(*ans)

t = int(input())
for _ in range(t):
    solve()