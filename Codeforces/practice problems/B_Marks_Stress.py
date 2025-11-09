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

    if n == 1:
        print(0 if k != 2 else n)
        return
    
    print(max(0, 3*n - k))
    
    


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()