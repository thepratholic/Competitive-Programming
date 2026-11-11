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
    arr = list(map(int, input().split()))

    if sum(arr) < 1:
        print(-1)
        return

    arr.sort()

    V = 0
    ans = []

    for i in range(n):
        if len(arr) == 1:
            x = arr.pop()
        else:
            mx = arr[-1]
            req = max(1 - V, 1 - V - mx)

            idx = bisect_left(arr, req)
            x = arr.pop(idx)

        V += x
        ans.append(V)

    print(*ans)

t = int(input())
for _ in range(t):
    solve()