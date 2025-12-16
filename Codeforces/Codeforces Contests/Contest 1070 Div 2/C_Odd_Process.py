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

    e, o = [], []

    for x in a:
        if x & 1:
            o.append(x)
        else:
            e.append(x)

    if len(e) == n:
        print(*([0] * n))
        return

    o.sort()
    e.sort()

    if len(o) == n:
        for k in range(1, n + 1):
            if k & 1:
                print(o[-1], end=" ")
            else:
                print(0, end=" ")
        print()
        return

    score = o[-1]
    ans = [0] * (n + 1)
    ans[1] = score

    for k in range(2, n + 1):
        if not e:
            ans[k] = ans[k - 2]
        else:
            ans[k] = ans[k - 1] + e.pop()

    if (sum(a) & 1) ^ 1:
        ans[n] = 0

    print(*ans[1:])


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()