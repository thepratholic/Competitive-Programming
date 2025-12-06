# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple


import sys, random
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, k, l, r, sall, sk = map(int, input().split())

    ans = [0] * n
    s_left = sall - sk
    s1 = sk // k
    r1 = sk % k

    if k == n:
        for i in range(k):
            ans[i] = s1 + (1 if r1 > 0 else 0)
            r1 -= 1

    
    else:
        s2 = (sall - sk) // (n - k)
        r2 = (s_left) % (n - k)

        for i in range(n):
            if i < k:
                ans[i] = s1 + (1 if r1 > 0 else 0)
                r1 -= 1

            elif k != n:
                ans[i] = s2 + (1 if r2 > 0 else 0)
                r2 -= 1

    random.shuffle(ans)
    print(*ans)


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()