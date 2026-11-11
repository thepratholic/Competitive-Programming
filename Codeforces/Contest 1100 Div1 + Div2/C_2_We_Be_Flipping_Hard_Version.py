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

    pref = 0
    suf = sum(a)

    best = -1
    best_ans = suf

    for i in range(n):
        if a[i] > 0:
            cur = pref + suf - 2 * a[i]

            if cur > best_ans:
                best_ans = cur
                best = i

        pref += abs(a[i])
        suf -= a[i]

    if best == -1:
        print(0)
        return
    
    ans = []
    last = 0

    if a[0] < 0:
        last = 1

    for i in range(1, best + 1):

        if a[i - 1] > 0 and (i == best or a[i] < 0):
            ans.append(i)

            if last:
                ans.append(last)

        if a[i] < 0:
            last = i + 1

    ans.append(best + 1)

    print(len(ans))
    print(*ans)



t = int(input())
for _ in range(t):
    solve()