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
    s = input().strip()

    cnt = [0] * 26

    for ch in s:
        cnt[ord(ch) - ord('a')] += 1

    last = s[-1]
    already = cnt[ord(last) - ord('a')]

    print(n - already)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()