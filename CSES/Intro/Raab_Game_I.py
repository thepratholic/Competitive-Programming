import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, a, b = map(int, input().split())

    if a + b > n:
        print("NO")
        return
    
    if (a == 0 or b == 0) and (a + b) != 0:
        print("NO")
        return
    
    print("YES")
    
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

    for i in range(a + 1, a + b + 1):
        print(i, end=" ")
    # print()

    for i in range(1, a + 1):
        print(i, end = " ")
    # print()

    for i in range(a + b + 1, n + 1):
        print(i, end = " ")
    print()
    



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()