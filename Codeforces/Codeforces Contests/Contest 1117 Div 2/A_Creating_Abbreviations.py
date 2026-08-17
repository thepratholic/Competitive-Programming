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
    n, m = map(int, input().split())

    words = [input().strip() for _ in range(n)]
    abbr = [input().strip() for _ in range(m)]

    avail = set()

    for word in words:
        avail.add(word[0].upper())

    rem = set(abbr)

    while True:
        changed = False

        for s in list(rem):
            if all(ch in avail for ch in s):
                rem.remove(s)

                avail.add(s[0])

                changed = True

        if not changed:
            break

    print("YES" if not rem else "NO")

    

t = int(input())
for _ in range(t):
    solve()