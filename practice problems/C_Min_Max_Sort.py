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

    mpp = defaultdict(int)
    for i, val in enumerate(a):
        mpp[val] = i


    if a == sorted(a) or n == 1:
        print(0)
        return
    
    l = (n + 1) // 2
    r = (n + 2) // 2


    while (l >= 1 and r <= n) and (l == r or (mpp[l] < mpp[l + 1] and mpp[r] > mpp[r - 1])):
        l -= 1
        r += 1

    print(l)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()