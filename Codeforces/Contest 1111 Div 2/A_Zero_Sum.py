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
    a = list(map(int, input().split()))

    if n & 1:
        print("NO")
        return
    
    cnt = 0

    for x in a:
        if x > 0:
            cnt -= 1

        else:
            cnt += 1

    if cnt % 4 == 0:
        print("YES")

    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()