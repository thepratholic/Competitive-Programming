import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from math import gcd, ceil, floor, sqrt, inf

input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = set(map(int, input().split()))

    if x in a:
        print(1)
    else:
        m = max(a)
        print(max(2, (x + m - 1) // m))

# TC : O(n)
# SC : O(n)

def main():
    multi = True
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

main()