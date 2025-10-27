import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    a, b, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mp1, mp2 = defaultdict(int), defaultdict(int)

    for boy in a:
        mp1[boy] += 1

    for girl in b:
        mp2[girl] += 1


    ans = 0
    for i in range(k):
        boy = a[i]
        girl = b[i]

        ans += (k - 1)
        ans -= (mp1[boy] - 1)
        ans -= (mp2[girl] - 1)

    print(ans // 2)    

    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()