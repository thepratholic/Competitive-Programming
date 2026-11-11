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

    d = [a[i + 1] - a[i] for i in range(n - 1)]

    i = 0
    while i < n - 1:
        j = i
        p = d[i] & 1

        while j < n - 1 and (d[j] & 1) == p:
            j += 1

        d[i : j] = sorted(d[i : j])
        i = j

    ans = [a[0]]
    for x in d:
        ans.append(ans[-1] + x)

    print(*ans)

t = int(input())
for _ in range(t):
    solve()