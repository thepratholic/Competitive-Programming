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

from sortedcontainers import SortedList

input = stdin.readline

def solve():
    # Write your solution here
    q, v = map(int, input().split())

    pq = []

    for _ in range(q):
        a = list(map(int, input().split()))

        if a[0] == 1:
            _, t, w = a

            k = w - t

            heappush(pq, -k)

        else:
            _, t = a

            if not pq:
                print(-1)
                continue

            k = -heappop(pq)
            print(min(v, k + t))




# t = int(input())
# for _ in range(t):
solve()