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
    n = int(input())
    a = input().strip()
    b = input().strip()

    count_a = a.count('1')
    count_b = b.count('1')

    if count_a != count_b:
        print("NO")
        return

    odd_a = sum(1 for i in range(n) if a[i] == '1' and (i + 1) % 2 == 1)
    odd_b = sum(1 for i in range(n) if b[i] == '1' and (i + 1) % 2 == 1)

    if odd_a == odd_b:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()