import sys
import math
import bisect
import heapq
import itertools
import collections
import functools
import operator
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt

input = lambda: sys.stdin.readline().strip()

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    seen = [0] * (n + 1)
    for num in a:
        seen[num] = 1

    ans = []
    miss = -1
    for i in range(1, n + 1):
        if seen[i] == 0:
            miss = i
            break

    if miss != -1:
        ans.append(miss)
        used = [0] * (n + 1)
        used[miss] = 1

    else:
        used = [0] * (n + 1)

    if len(ans) < k:
        for i in range(1, n + 1):
            if used[i] == 0 and i != a[-1]:
                ans.append(i)
                used[i] = 1
                break


    for i in range(1, n + 1):
        if len(ans) >= k:
            break

        if used[i] == 0:
            ans.append(i)
            used[i] = 1


    print(" ".join(map(str, ans)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
