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


def f_xor(p):
    n = len(p)
    seen = [False] * (n + 2)
    mex = 0
    x = 0

    for v in p:
        seen[v] = True
        while seen[mex]:
            mex += 1
        x ^= mex

    return x


def brute(n, k):
    for p in permutations(range(n)):
        if f_xor(list(p)) == k:
            return list(p)
        
    return None


def solve():
    n, k = map(int, input().split())

    if n <= 3:
        res = brute(n, k)
        if res is None:
            print("NO")
        else:
            print("YES")
            print(*res)
        return

    t = n ^ k

    lim = 1
    while lim < n:
        lim <<= 1

    if t >= lim:
        print("NO")
        return

    if t == 0:
        special = []
    elif t < n:
        special = [t]
    else:
        x = 1 << (t.bit_length() - 1)
        special = [t ^ x, x]
        special.sort()

    used = [False] * n
    used[0] = True

    for x in special:
        used[x] = True

    ans = []

    for i in range(n):
        if not used[i]:
            ans.append(i)

    ans.append(0)

    ans.extend(special)

    print("YES")
    print(*ans)


for _ in range(int(input())):
    solve()