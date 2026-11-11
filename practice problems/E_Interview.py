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

def query(k, l, r):
    print("? ", k, end=" ")
    for i in range(l, r + 1):
        print(i, end=" ")
    sys.stdout.flush()
    s = int(input())
    return s

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]


    low, high = 1, n
    ans = n

    while low <= high:
        mid = (low + high) >> 1

        res = query(mid - low + 1, low, mid)

        if res == pref[mid] - pref[low - 1]:
            low = mid + 1

        else:
            ans = mid
            high = mid - 1

    print("! ", ans, flush=True)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()