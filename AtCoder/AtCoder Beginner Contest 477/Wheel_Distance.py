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
    n, q = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    adj = [[] for _ in range(n + 2)]

    for i in range(1, n + 1):
        j = i % n + 1

        adj[i].append((j, a[i - 1]))
        adj[j].append((i, a[i - 1]))

    for i in range(1, n + 1):
        adj[i].append((n + 1, b[i - 1]))
        adj[n + 1].append((i, b[i - 1]))

    INF = float('inf')

    best = [INF] * (n + 2)
    best[n + 1] = 0

    pq = [(0, n + 1)]

    while pq:
        dist, u = heappop(pq)

        if dist != best[u]:
            continue

        for v, w in adj[u]:
            new_dist = dist + w

            if new_dist < best[v]:
                best[v] = new_dist
                heappush(pq, (new_dist, v))

    pref = [0] * (n + 1)

    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    total = pref[n]

    for _ in range(q):
        s, t = map(int, input().split())

        if t == n + 1:
            print(best[s])
            continue

        case1 = best[s] + best[t]

        l = min(s, t)
        r = max(s, t)

        case2 = pref[r - 1] - pref[l - 1]

        case3 = total - case2

        print(min(case1, case2, case3))


solve()