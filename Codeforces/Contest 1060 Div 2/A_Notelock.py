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
    n, k = map(int, input().split())
    s = input().strip()

    last = -10**9
    ans = 0
    for i, ch in enumerate(s, start=1):
        if ch == '1':
            if i - last >= k:
                ans += 1
                last = i
            else:
                last = i
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()