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
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter()

    for x in a:
        for _ in range(100):
            s = 0
            while x:
                d = x % 10
                s += d * d
                x //= 10
            x = s
            
        freq[x] += 1

    ans = 0
    for cnt in freq.values():
        ans += cnt * (cnt - 1) // 2

    print(ans)


t = int(input())
for _ in range(t):
    solve()