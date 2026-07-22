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


input = sys.stdin.readline

INF = 10 ** 18


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    lo, hi = 0, INF
    ans = 0

    while lo <= hi:
        mid = (lo + hi) >> 1

        bin_arr = [0] * n
        for i in range(n):
            if a[i] >= mid and b[i] >= mid:
                bin_arr[i] = 1
            elif a[i] < mid and b[i] < mid:
                bin_arr[i] = -1
            else:
                bin_arr[i] = 0

        zero = 0
        pos = 0
        i = 0
        while i < n:
            if bin_arr[i] == 1:
                pos += 1
                i += 1
            elif bin_arr[i] == 0:
                zero += 1
                i += 1
            else:
                pos -= 1
                while i + 1 < n and (bin_arr[i + 1] == -1 or bin_arr[i + 1] == 0):
                    i += 1
                i += 1

        if (pos + zero > 0 and pos > 0) or (pos > 1):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


t = int(input())
for _ in range(t):
    solve()