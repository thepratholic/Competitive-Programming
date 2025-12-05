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
    n, k = map(int, input().split())
    s = input().strip()
    
    block_until = -1
    ans = 0
    
    for i in range(n):
        if s[i] == '1':
            block_until = i + k
        else:
            if i > block_until:
                ans += 1

    print(ans)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()