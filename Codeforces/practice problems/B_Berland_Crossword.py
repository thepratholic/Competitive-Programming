import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline



def solve():
    n, u, r, d, l = map(int, input().split())

    def isValid(x):
        return 0 <= x <= n-2

    for tl in range(2):
        for tr in range(2):
            for br in range(2):
                for bl in range(2):

                    u_ = u - (tl + tr)
                    r_ = r - (tr + br)
                    d_ = d - (br + bl)
                    l_ = l - (tl + bl)

                    if isValid(u_) and isValid(r_) and isValid(d_) and isValid(l_):
                        print("YES")
                        return
                    
    print("NO")



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()