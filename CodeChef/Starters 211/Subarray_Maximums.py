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

    if s[0] == '0' or s[-1] == '0':
        print(-1)
        return

    p = [0] * n
    pos = [0] * (n + 1)

    for k in range(1, n + 1):
        p[n - k] = k
        pos[k] = n - k


    for i in range(n - 1, 1, -1):
        if s[i - 1] == '0':
            pos_i = pos[i]
            pos_ip1 = pos[i + 1]
            p[pos_i], p[pos_ip1] = p[pos_ip1], p[pos_i]
            pos[i], pos[i + 1] = pos[i + 1], pos[i]

    print(*p)
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()