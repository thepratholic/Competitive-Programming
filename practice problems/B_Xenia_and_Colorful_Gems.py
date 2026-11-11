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
    nr, ng, nb = map(int, input().split())
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))

    r.sort()
    g.sort()
    b.sort()

    ans = 10 ** 30

    def get(x, y, z):
        return (x - y) ** 2 + (y - z) ** 2 + (z - x) ** 2

    def solve(mid, right, left):

        nonlocal ans

        for x in mid:
            idx = bisect_left(right, x)

            if idx == len(right):
                continue

            j = bisect_right(left, x)

            if j == 0:
                continue

            y = right[idx]
            z = left[j - 1]

            ans = min(ans, get(x, y, z))

    solve(r, g, b)
    solve(r, b, g)
    solve(g, r, b)
    solve(g, b, r)
    solve(b, r, g)
    solve(b, g, r)

    print(ans)


t = int(input())
for _ in range(t):
    solve()