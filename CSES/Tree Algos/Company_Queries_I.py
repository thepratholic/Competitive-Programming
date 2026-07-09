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
    n, q = map(int, input().split())
    a = [-1, -1] + list(map(int, input().split()))

    up = [[-1] * 20 for _ in range(n + 1)]

    for i, v in enumerate(a):
        if i > 1:
            up[i][0] = v # current node ka 2^0th ancestor

    # pre-processing
    for k in range(1, 20):
        for node in range(1, n + 1):
            if up[node][k - 1] != -1:
                up[node][k] = up[up[node][k - 1]][k - 1]

    def get(node, k):
        for bit in range(32):
            if k & (1 << bit):
                if node != -1:
                    node = up[node][bit]

        return node
    
    for _ in range(q):
        x, k = map(int, input().split())

        print(get(x, k))

t = 1
for _ in range(t):
    solve()