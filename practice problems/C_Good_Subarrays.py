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

    mpp = defaultdict(int)
    mpp[0] = 1

    ans, pref = 0, 0
    for ch in s:

        pref += (ord(ch) - ord('0')) - 1
        ans += mpp[pref]
        mpp[pref] += 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()