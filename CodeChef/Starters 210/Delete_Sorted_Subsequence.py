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
    
    if n == 0:
        print(0)
        return
        
    s = input().strip()
    
    bal, bal2 = 0, 0
    ans = 0
    for ch in s:
        if ch == '0':
            bal += 1
            bal2 += 1

        else:
            bal -= 1
            bal2 = max(bal2 - 1, 0)

        
        if bal < 0:
            ans = 1

    if bal2 > 0:
        ans += 1

    print(ans)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()