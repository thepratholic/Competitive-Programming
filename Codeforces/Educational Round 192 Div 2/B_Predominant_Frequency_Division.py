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

    can1 = [0] * n
    cnt1 = cnt23 = 0

    for i in range(n):
        if a[i] == 1:
            cnt1 += 1

        else:
            cnt23 += 1

        can1[i] = (cnt1 >= cnt23)

        if cnt1 < cnt23:
            cnt1 = 0
            cnt23 = 0
            
    can2 = [0] * n
    cnt12 = 0
    cnt3 = 0

    for i in range(n - 2, -1, -1):
        if a[i] == 3:
            cnt3 += 1

        else:
            cnt12 += 1

        can2[i] = (cnt12 >= cnt3)

        if cnt12 < cnt3:
            cnt12 = 0
            cnt3 = 0

    will = False
    for i in range(n - 1):
        if can1[i] and can2[i + 1]:
            will = True

    print("YES" if will else "NO")

t = int(input())
for _ in range(t):
    solve()