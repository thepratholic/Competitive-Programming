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
    s, c = map(str, input().split())
    s = list(s)

    n, m = len(s), len(c)

    
    def check(s):
        for i in range(n):
            if i == m:
                return False
            
            if s[i] < c[i]:
                return True
            
            if c[i] < s[i]:
                return False
            
        if n < m:
            return True
        
        else:
            return False
        
    
    for i in range(n): # traverse karo in s
        if i == m:
            print("---")
            return
        
        idx, ch = i, s[i]

        for j in range(i + 1, n):
            if ch > s[j]: # means iss string mein swap ho skta hai, chota char hai
                ch = s[j]
                idx = j


        if ch < c[i]:
            s[i], s[idx] = s[idx], s[i]
            print("".join(s))
            return
        
        if s[i] > c[i]:
            for j in range(n):
                if j == i: continue

                st = list(s)
                st[i], st[j] = st[j], st[i]

                if check("".join(st)):
                    print("".join(st))
                    return
                
            print("---")
            return
        
    if n == m:
        print("---")
    else:
        print("".join(s))

t = int(input())
for _ in range(t):
    solve()