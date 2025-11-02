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
    b = list(map(int, input().split()))

    if n == 1:
        print(max(a[0],  b[0]))
        return
    
    m1, m2 = 0, 0
    for i in range(n):
        c1, c2 = a[i] + m2, b[i] + m1

        m1 = max(m1, c1)
        m2 = max(m2, c2)

    print(max(m1, m2))

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()