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
    n, k = map(int, input().split())

    rem = n - (k - 3)

    ans = [1] * (k - 3)

    if rem & 1:
        ans.extend([rem // 2, rem // 2, 1])

    else:
        if (rem // 2) % 2 == 0:
            ans.extend([rem // 2, rem // 4, rem // 4])

        else:
            ans.extend([2, rem // 2 - 1, rem // 2 - 1])

    print(*ans)

t = int(input())
for _ in range(t):
    solve()