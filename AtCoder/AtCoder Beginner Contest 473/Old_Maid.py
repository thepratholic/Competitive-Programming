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

    freq = Counter(a)

    ans = 0

    for num, count in freq.items():
        if count % 2 == 1:
            ans += num

    print(ans)

# t = int(input())
# for _ in range(t):
solve()