import sys
import os
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    labs = [tuple(map(int, input().split())) for _ in range(n)]

    def check(x):
        total_need = 0

        for a, b, c in labs:
            s = a + b + c

            if s >= x:
                continue

            d = x - s

            if a <= b <= c:
                if a == c:
                    return False

                p = min(b - a, c - b) + 1
                need = d + 2 * p
            else:
                need = d

            total_need += need

            if total_need > k:
                return False

        return True

    lo = min(a + b + c for a, b, c in labs)
    hi = max(a + b + c for a, b, c in labs) + k

    ans = -1

    while lo <= hi:
        mid = (lo + hi) >> 1

        if check(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


t = int(input())

for _ in range(t):
    solve()