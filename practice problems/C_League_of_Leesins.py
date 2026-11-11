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

    triplets = []
    freq = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 2):
        a, b, c = map(int, input().split())

        triplets.append((a, b, c))

        freq[a] += 1; freq[b] += 1; freq[c] += 1

        adj[a].extend((b, c))
        adj[b].extend((a, c))
        adj[c].extend((a, b))

    last = second_last = None

    for a, b, c in triplets:
        arr = [a, b, c]

        for i in range(3):
            if freq[arr[i]] != 1:
                continue

            for j in range(3):
                if i == j:
                    continue

                if freq[arr[j]] == 2:
                    last = arr[i]
                    second_last = arr[j]
                    break

            if last is not None:
                break

        if last is not None:
            break

    vis = [False] * (n + 1)
    vis[last] = True
    vis[second_last] = True

    pq = []

    for i in range(1, n + 1):
        if not vis[i]:
            heappush(pq, (freq[i], i))

    ans = []

    while pq:
        f, u = heappop(pq)

        if vis[u]:
            continue

        if f != freq[u]:
            continue

        vis[u] = True
        ans.append(u)

        for v in adj[u]:
            if not vis[v]:
                freq[v] -= 1
                heappush(pq, (freq[v], v))

    ans.append(second_last)
    ans.append(last)

    print(*ans)


# t = int(input())
# for _ in range(t):
solve()