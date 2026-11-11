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
    s = list(input().strip())
    n = len(s)
    ans = 0
    
    if s[0] == 'u':
        s[0] = 's'
        ans += 1
    if s[-1] == 'u':
        s[-1] = 's'
        ans += 1
        
    for i in range(n - 1):
        if s[i] == 'u' and s[i+1] == 'u':
            s[i+1] = 's'
            ans += 1
            
    print(ans)


if __name__ == '__main__':
    t_str = input().strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()