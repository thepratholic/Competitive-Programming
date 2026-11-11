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
    can = True
    for i in range(1, n - 1, 2):
        if a[i] != a[i+1]:
            can = False
            break
            
    if can:
        print("YES")
    else:
        print("NO")
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()