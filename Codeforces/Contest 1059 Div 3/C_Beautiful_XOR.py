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
    a, b = map(int, input().split())

    if a == b:
        print(0)
        return
    
    c = a ^ b

    def msb_pos(x):
        return x.bit_length() - 1
    
    msbA = msb_pos(a)
    msbB = msb_pos(b)

    if msbA < msbB:
        print(-1)
        return
    
    if a >= c:
        print(1)
        print(c)
        return
    
    else:
        print(2)
        print(b, a)
        return

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()