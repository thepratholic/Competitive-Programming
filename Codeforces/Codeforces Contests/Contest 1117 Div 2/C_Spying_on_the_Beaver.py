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

    par = [-1, -1] + list(map(int, input().split()))

    child = [[] for _ in range(n + 1)]

    for i in range(2, n + 1):
        child[par[i]].append(i)

    m = int(input())
    dams = list(map(int, input().split()))

    is_dam = [False] * (n + 1)
    cnt = [0] * (n + 1)

    for x in dams:
        is_dam[x] = True
        cnt[x] = 1

    for u in range(n, 1, -1):
        cnt[par[u]] += cnt[u]

    cameras = []

    for u in range(1, n + 1):
        active = []

        for v in child[u]:
            if cnt[v] > 0:
                active.append(v)

        deg = (1 if is_dam[u] else 0) + len(active)

        if deg > 1:
            need = deg - 1

            for i in range(need):
                cameras.append(active[i])

    print(len(cameras), *cameras)


t = int(input())
for _ in range(t):
    solve()