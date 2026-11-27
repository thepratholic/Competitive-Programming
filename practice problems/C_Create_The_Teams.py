import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from math import gcd, ceil, floor, sqrt, inf

input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    cur = 0
    teams = 0

    for i in a:
        cur += 1

        if cur * i >= x:
            teams += 1
            cur = 0

    print(teams)

# TC : O(n log n)
# SC : O(n)

def main():
    multi = True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

main()