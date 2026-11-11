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

    if n == 1:
        print(a[0])
        return
    
    dp = [[0, 0] for _ in range(n + 5)]
    for i in range(n - 1, -1, -1):
        t1 = a[i] + dp[i + 1][1]
        t2 = a[i]
        if i + 1 < n:
            t2 += a[i + 1] 
        t2 += dp[i + 2][1]

        dp[i][0] = min(t1, t2)

        y1 = dp[i + 1][0]  
        y2 = dp[i + 2][0]  
        dp[i][1] = min(y1, y2)

    print(dp[0][0])

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()