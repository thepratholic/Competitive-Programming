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

def f(arr, m):
    res = []

    for x in arr:
        base = x
        cnt = 1

        while base % m == 0:
            base //= m
            cnt *= m

        if res and res[-1][0] == base:
            res[-1][1] += cnt

        else:
            res.append([base, cnt])

    return res

def solve():
    # Write your solution here
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = int(input())
    b = list(map(int, input().split()))

    if f(a, m) == f(b, m):
        print("Yes")

    else:
        print("No")
    
    

t = int(input())
for _ in range(t):
    solve()