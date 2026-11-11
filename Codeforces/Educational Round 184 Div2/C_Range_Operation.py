import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    a = list(map(int, input().split()))
    # s = sum(a)

    pref = 0
    ans = 0
    mx_val = 0

    for i in range(1, n + 1):
        mx_val = max(mx_val, -(i * i) + i + pref)
        
        pref += a[i - 1]
        ans = max(ans, (i * i) + i - pref + mx_val)

    print(pref + ans)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
