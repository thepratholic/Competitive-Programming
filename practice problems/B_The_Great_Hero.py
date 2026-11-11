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
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    damage = 0

    for i in range(n):
        hits = (b[i] + A - 1) // A
        damage += (hits * a[i])

    print("YES" if B + max(a) > damage else "NO")

t = int(input())
for _ in range(t):
    solve()