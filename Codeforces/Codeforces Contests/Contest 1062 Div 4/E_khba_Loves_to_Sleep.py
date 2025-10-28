import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n, k, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    def ok(d):
        iv = []
        for v in a:
            l, r = max(0, v - d + 1), min(x, v + d - 1)
            if l <= r:
                iv.append((l, r))
        if not iv:
            return x + 1 >= k
        iv.sort()
        m = []
        cl, cr = iv[0]
        for l, r in iv[1:]:
            if l <= cr + 1:
                cr = max(cr, r)
            else:
                m.append((cl, cr))
                cl, cr = l, r
        m.append((cl, cr))
        bad = sum(r - l + 1 for l, r in m)
        return (x + 1 - bad) >= k

    lo, hi, ans = 0, x, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    d = ans
    iv = []
    for v in a:
        l, r = max(0, v - d + 1), min(x, v + d - 1)
        if l <= r:
            iv.append((l, r))
    if not iv:
        print(" ".join(map(str, range(k))))
        return
    iv.sort()
    m = []
    cl, cr = iv[0]
    for l, r in iv[1:]:
        if l <= cr + 1:
            cr = max(cr, r)
        else:
            m.append((cl, cr))
            cl, cr = l, r
    m.append((cl, cr))

    tp = []
    s, e = 0, m[0][0] - 1
    for p in range(s, e + 1):
        if len(tp) < k:
            tp.append(str(p))
        else:
            break
    for i in range(len(m) - 1):
        if len(tp) == k:
            break
        s, e = m[i][1] + 1, m[i + 1][0] - 1
        for p in range(s, e + 1):
            if len(tp) < k:
                tp.append(str(p))
            else:
                break
    if len(tp) < k:
        s, e = m[-1][1] + 1, x
        for p in range(s, e + 1):
            if len(tp) < k:
                tp.append(str(p))
            else:
                break
    print(" ".join(tp))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
