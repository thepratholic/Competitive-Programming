# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    q = int(input())

    st = {0}
    mpp = defaultdict(int)

    for _ in range(q):

        op, val = input().split()
        val = int(val)
        if op == '+':
            st.add(val)

        elif op == '?':

            mex = mpp.get(val, 0)

            while mex in st:
                mex += val

            mpp[val] = mex

            print(mex)

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()