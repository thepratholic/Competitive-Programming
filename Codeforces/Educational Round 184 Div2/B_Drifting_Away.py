import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        return

    bad = {'><', '**', '>*', '*<'}
    for i in range(n - 1):
        if s[i:i+2] in bad:
            print(-1)
            return

    left = 0
    for ch in s:
        if ch == '>':
            break
        left += 1

    right = 0
    for ch in reversed(s):
        if ch == '<':
            break
        right += 1

    print(max(left, right))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
