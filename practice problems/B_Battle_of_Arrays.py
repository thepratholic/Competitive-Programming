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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    alice_pq = []
    bob_pq = []

    for x in a:
        heappush(alice_pq, -x)

    for x in b:
        heappush(bob_pq, -x)

    turn = True # true means alice, else bob
    while alice_pq and bob_pq:
        a = -heappop(alice_pq)
        b = -heappop(bob_pq)

        if turn:
            # means alice

            if b <= a:
                heappush(alice_pq, -a)

            else:
                b -= a
                heappush(alice_pq, -a)
                heappush(bob_pq, -b)

            turn = not turn

        else:

            if a <= b:
                heappush(bob_pq, -b)

            else:
                a -= b
                heappush(bob_pq, -b)
                heappush(alice_pq, -a)

            turn = not turn

    
    if alice_pq:
        print("Alice")
    else:
        print("Bob")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()