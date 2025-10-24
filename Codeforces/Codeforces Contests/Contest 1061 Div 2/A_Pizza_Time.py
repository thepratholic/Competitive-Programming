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

def solve():
    n = int(input())

    ans = 0
    while n >= 3:
        ans += (n // 3)
        n -= (2 * (n // 3))

    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()