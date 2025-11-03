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

    a.sort()
    ans = 1

    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()