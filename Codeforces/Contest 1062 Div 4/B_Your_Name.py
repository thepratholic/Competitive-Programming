import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    sz = int(input())
    s, t = input().strip().split()

    freq = defaultdict(int)

    for ch in s:
        freq[ch] += 1

    for ch in t:
        freq[ch] -= 1

    for v in freq.values():
        if v != 0:
            print("NO")
            return
        
    print("YES")

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        solve()
