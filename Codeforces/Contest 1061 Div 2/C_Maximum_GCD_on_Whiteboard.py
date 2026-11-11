import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = [0] * (n + 1)
    pref = [0] * (n + 1)

    for i, val in enumerate(a):
        cnt[val - 1] += 1

    for i in range(n):
        pref[i + 1] = pref[i] + cnt[i]

    for g in range(n, 1, -1):
        x = min(n, 4 * g - 1)
        rem = pref[x]

        for i in range(1, 4):
            if g * i > n: break
            rem -= cnt[i * g - 1]

        if rem <= k:
            print(g)
            return
        
    print(1)
    return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()