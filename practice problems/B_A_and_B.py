# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())

    if a == b:
        print(0)
        return
    
    s = abs(a - b)

    for i in range(10 ** 5):
        y = i * (i + 1) // 2

        if y >= s and y % 2 == s % 2:
            print(i)
            break


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()