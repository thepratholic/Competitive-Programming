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

    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x & 1]

    even.extend(odd)

    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if gcd(even[i], 2 * even[j]) > 1:
                ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()