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

    # if all(ch for ch in s) == '0':
    #     print(n)
    #     return
    
    # if all(ch for ch in s) == '1':
    #     print(0)
    #     return
    

    first_one = -1

    for i in range(n):
        if s[i] == '1':
            first_one = i
            break
    


    ans = 0
    for i in range(first_one if first_one != -1 else n):
        if s[i] == '0': ans += 1

    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()