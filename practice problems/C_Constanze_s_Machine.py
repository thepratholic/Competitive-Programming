import sys
import math
import bisect
import heapq
import itertools
import collections
import functools
import operator
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt

MOD = 10**9 + 7

def solve():
    s = input().strip()

    n = len(s)
    for c in s:
        if c == 'w' or c == 'm':
            print(0)
            return
        
    dp = {}
    dp[0] = 1
    dp[-1] = 1
    
    for i in range(1, n):
        dp[i] = dp[i - 1]

        if s[i] == s[i - 1] and (s[i] == 'n' or s[i] == 'u'):
            dp[i] = (dp[i] + dp[i - 2]) % MOD

    print(dp[n - 1] % MOD)



def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()