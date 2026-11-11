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

    
    s_sum = sum(a) - a[0]
    p_val = 0
    ans = -s_sum
    
    for k in range(n - 1):
        s_sum -= a[k+1]
        
        if k == 0:
            p_val += a[k]
        else:
            p_val += abs(a[k])
            
        ans = max(ans, p_val - s_sum)

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()