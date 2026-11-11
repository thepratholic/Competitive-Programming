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

    if a == sorted(a):
        print(*a)
        return
    
    parity = [0, 0]
    for i, val in enumerate(a):
        if val & 1:
            parity[1] += 1
        else:
            parity[0] += 1

    if parity[0] == 0 and parity[1] > 0:
        print(*a)
        return
    elif parity[0] > 0 and parity[1] == 0:
        print(*a)
        return
    
    else:
        a = sorted(a)
        print(*a)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()