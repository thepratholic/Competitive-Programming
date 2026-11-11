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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0

    for ai, bi in zip(a, b):
        x ^= (ai ^ bi)
    if x == 0:
        print("Tie")
        return
    
    k = x.bit_length() - 1
    last = -1
    cnt = 0

    for i, (ai, bi) in enumerate(zip(a, b)):
        if ((ai ^ bi) >> k) & 1:
            last = i
            cnt += 1
            
    if cnt % 2 == 0:
        print("Tie")
    else:
        if last % 2 == 0:
            print("Ajisai")
        else:
            print("Mai")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()