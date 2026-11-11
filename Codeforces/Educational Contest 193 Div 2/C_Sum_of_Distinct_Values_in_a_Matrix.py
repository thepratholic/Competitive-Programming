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
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    la = []
    lb = []
    lab = []

    i = j = 0

    while i < x and j < y:
        if a[i] == b[j]:
            lab.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            la.append(a[i])
            i += 1
        else:
            lb.append(b[j])
            j += 1

    la += a[i:]
    lb += b[j:]

    la.reverse()
    lb.reverse()
    lab.reverse()

    def calc(r, c):
        aa = la[:r]
        bb = lb[:c]

        z = []
        i = j = 0

        while i < len(aa) and j < len(bb):
            if aa[i] >= bb[j]:
                z.append(aa[i])
                i += 1
            else:
                z.append(bb[j])
                j += 1

        z += aa[i:]
        z += bb[j:]

        pa = [0]
        for v in lab:
            pa.append(pa[-1] + v)

        pz = [0]
        for v in z:
            pz.append(pz[-1] + v)

        ans = 0
        for k in range(min(len(lab), r + c) + 1):
            rem = min(r + c - k, len(z))
            ans = max(ans, pa[k] + pz[rem])

        return ans

    print(max(calc(n, m - 1), calc(n - 1, m)))

t = int(input())
for _ in range(t):
    solve()