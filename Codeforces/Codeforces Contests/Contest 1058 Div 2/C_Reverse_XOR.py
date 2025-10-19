import sys
import math
import bisect
import heapq
import itertools
import collections
import functools
import operator
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt

input = lambda: sys.stdin.readline().strip()


def isPalin(s, i, j):
    # n = len(s)
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def solve():
    n = int(input())

    if n == 0:
        print("YES")
        return
    
    b = ""
    s = bin(n)[2:]
    s = s.rstrip('0')

    ones_count = s.count("1")

    if s == s[::-1] and ones_count % 2 == 0:
        print("YES")
    else:
        print("NO")


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()