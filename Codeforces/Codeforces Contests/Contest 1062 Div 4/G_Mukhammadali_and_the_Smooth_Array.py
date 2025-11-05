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
    c = list(map(int, input().split()))

    dp = [0] * n

    for i in range(n):
        dp[i] = c[i]

        for j in range(i):
            if a[j] <= a[i]:
                dp[i] = max(dp[i] , dp[j] + c[i])

    print(sum(c) - max(dp))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()