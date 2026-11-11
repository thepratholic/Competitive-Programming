# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


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
    p = list(map(int, input().split()))
    x = input().strip()
    
    a, b = 0, 0

    while p[a] != 1:
        a += 1

    while p[b] != n:
        b += 1

    if x[0] == '1' or x[-1] == '1' or x[a] == '1' or x[b] == '1':
        print(-1)
        return
    
    a += 1
    b += 1

    ans = [[1, a], [1, b], [a, n], [b, n], [min(a, b), max(a, b)]]

    print(5)
    for i, (x, y) in enumerate(ans):
        print(x, y)



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()




