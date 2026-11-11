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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k >= 3:
        print(0)
        return
    
    a.sort()
    ans = a[0]

    for i in range(1, n):
        ans = min(ans, a[i] - a[i - 1])

    if k == 1 or ans == 0:
        print(ans)
        return

    for i in range(n):
        for j in range(i):
            d = a[i] - a[j]
            ans = min(ans, d)

            idx = bisect_left(a, d)

            if idx - 1 >= 0:
                ans = min(ans, abs(d - a[idx - 1]))

            if idx < n:
                ans = min(ans, abs(a[idx] - d))


            if ans == 0: break

        if ans == 0:
            break

    print(ans)




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()