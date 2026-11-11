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
    a = list(map(int, input().split()))

    zeros = a.count(0)

    if zeros < 2:
        print(-1)
        return

    if a[0] == 0 and a[-1] == 0:
        print(0)
        return

    if a[0] == 0 or a[-1] == 0:
        print(1)
        return

    print(2)


t = int(input())
for _ in range(t):
    solve()