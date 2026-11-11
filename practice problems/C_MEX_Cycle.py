import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline


def f(st):
    ans = 0
    while ans in st:
        ans += 1
    return ans


def solve():
    n, x, y = map(int, input().split())

    x -= 1
    y -= 1

    adj = defaultdict(set)
    adj[x].add(y)
    adj[y].add(x)

    for i in range(n):
        adj[i].add((i + 1) % n)
        adj[i].add((i + n - 1) % n)

    
    ans = [-1] * n

    for i in range(n):
        st = set()

        for frd in adj[i]:
            if ans[frd] != -1:
                st.add(ans[frd])

        ans[i] = f(st)

    print(*ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()