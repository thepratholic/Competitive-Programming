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

def solve():
    n = int(input())
    s = input().strip()

    zeros = s.count('0')
    print(zeros)

    for i in range(n):
        if s[i] == '0':
            print(i + 1, end=" ")

    print()

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()