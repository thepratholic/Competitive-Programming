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
    s = input().strip()

    if s.count("0") == 0:
        print(0)
        return

    s2 = s + s
    last1 = -10**9
    dist = [0] * (2*n)

    for i in range(2*n):
        if s2[i] == '1':
            last1 = i
        dist[i] = i - last1

    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans = max(ans, dist[i + n])

    print(ans)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()