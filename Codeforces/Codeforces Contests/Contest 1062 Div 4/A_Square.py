import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    a, b, c, d = map(int, input().split())

    if a == b == c == d:
        print("YES")
        return
    else:
        print("NO")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()