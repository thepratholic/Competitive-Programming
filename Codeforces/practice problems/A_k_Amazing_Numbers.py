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

    pos = defaultdict(list)

    for i in range(n):
        pos[a[i]].append(i)

    ans = [-1] * n

    for i in range(1, n + 1):
        if len(pos[i]) == 0: continue

        vals = pos[i]
        mx = vals[0] + 1

        for j in range(1, len(vals)):
            mx = max(mx, vals[j] - vals[j - 1])

        mx = max(mx, n - vals[-1])

        j = mx - 1
        while j < n:
            if ans[j] != -1: break
            else: ans[j] = i

            j += 1

    print(*ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()