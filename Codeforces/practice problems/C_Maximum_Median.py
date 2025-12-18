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

    a.sort()

    low, high = a[n // 2], a[n // 2] + k
    ans = a[n // 2]


    def check(mid):
        moves = 0
        for i in range(n // 2, n):
            if a[i] < mid:
                moves += (mid - a[i])

                if moves > k: return False

        return True

    while low <= high:
        mid = (low + high) >> 1

        if check(mid):
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    print(ans)

if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    solve()