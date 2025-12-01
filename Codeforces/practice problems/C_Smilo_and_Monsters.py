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
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum_ = sum(a)
    ans = ceil(sum_ / 2)

    for_higher = sum_ // 2

    for x in reversed(a):
        if for_higher <= 0:
            break

        for_higher -= x
        ans += 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()