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
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [(a[i], i) for i in range(n)]

    a.sort()
    b.sort()

    ans = [0] * n

    for i in range(n):
        value, idx = a[i]
        ans[idx] = b[i]

    print(*ans)


t = int(input())

for _ in range(t):
    solve()