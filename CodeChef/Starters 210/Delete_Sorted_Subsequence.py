import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def is_balanced(s, n):
    bal = 0
    for i in range(n):
        if s[i] == '0':
            bal += 1
        else:
            bal -= 1
        
        if bal < 0:
            return False
            
    return bal == 0

def solve():
    n = int(input())
    
    if n == 0:
        print(0)
        return
        
    s = input().strip()
    
    if is_balanced(s, n):
        print(0)
        return

    first_bad_1 = n + 1
    bal = 0
    for i in range(n):
        if s[i] == '0':
            bal += 1
        else:
            bal -= 1
        
        if bal < 0:
            first_bad_1 = i
            break

    last_bad_0 = -1
    bal_r = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            bal_r += 1
        else:
            bal_r -= 1
        
        if bal_r < 0:
            last_bad_0 = i
            break
            
    if first_bad_1 < last_bad_0:
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()