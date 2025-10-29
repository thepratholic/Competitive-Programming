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
    
    arr = sorted([(a[i], i) for i in range(n)])
    ans = [0] * n
    
    for i in range(n):
        if i == 0 or i == n - 1:
            ans[arr[i][1]] = -1
        else:
            left = (arr[i - 1][0] + arr[i][0]) // 2
            right = (arr[i][0] + arr[i + 1][0]) // 2
            ans[arr[i][1]] = right - left
    
    print(*ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()