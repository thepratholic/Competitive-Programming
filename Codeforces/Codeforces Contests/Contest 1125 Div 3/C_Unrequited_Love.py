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

    m = n - 4

    if m <= 0:
        print(0)
        return

    groups = defaultdict(list)

    for i in range(m):
        val = a[i] + a[i + 2] - a[i + 4]
        groups[val].append(i)

    ans = 0

    for arr in groups.values():

        even = []
        odd = []

        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        ans += len(even) * len(odd)

        for v in (even, odd):
            l = 0

            for r in range(len(v)):
                while v[r] - v[l] >= 6:
                    l += 1

                ans += l

    print(ans)

t = int(input())
for _ in range(t):
    solve()