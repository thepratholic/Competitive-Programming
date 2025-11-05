import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    w, p, k = map(int, input().split())

    ans = 0
    while k > 0 and w > 0:
        ans += 2
        w -= 1
        k -= 1

    while k > 0:
        p -= 1
        ans += 1
        k -= 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()