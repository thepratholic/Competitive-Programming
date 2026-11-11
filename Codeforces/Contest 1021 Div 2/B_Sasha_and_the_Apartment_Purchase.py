import sys, io, os
import math
import bisect
import heapq
import string
import re
from decimal import *
from random import randrange, choice, shuffle
from types import GeneratorType
from collections import defaultdict, Counter, deque

input = sys.stdin.readline

def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LI(): return list(input().split())
def LII(): return list(map(int, input().split()))
def GMI(): return map(lambda x: int(x) - 1, input().split())
def LGMI(): return list(map(lambda x: int(x) - 1, input().split()))
def WRITE(out): return print('\n'.join(map(str, out)))
def WS(out): return print(' '.join(map(str, out)))
def WNS(out): return print(''.join(map(str, out)))
def WSNOPRINT(out): return ''.join(map(str, out))

def solve():
    n, k = MII()
    A = LII()
    A.sort()

    C = []
    start_c = n & 1
    for c in range(start_c, k + 1, 2):
        m = n - c
        L0 = (m + 1) // 2
        l = A[L0 - 1]
        r = A[L0 + c]
        C.append((l, r))

    C.sort()
    merged_C = []
    for l, r in C:
        if not merged_C or l > merged_C[-1][1] + 1:
            merged_C.append([l, r])
        else:
            merged_C[-1][1] = max(merged_C[-1][1], r)

    st = [seg[0] for seg in merged_C]
    en = [seg[1] for seg in merged_C]
    def covered(v):
        i = bisect.bisect_right(st, v) - 1
        return i >= 0 and v <= en[i]

    II_list = []
    p = (n - 1) & 1
    for c in range(p, k + 1, 2):
        m = n - c
        L0 = (m + 1) // 2
        l = L0
        r = L0 + c
        II_list.append((l, r))

    II_list.sort()
    merged_II = []
    for l, r in II_list:
        if not merged_II or l > merged_II[-1][1] + 1:
            merged_II.append([l, r])
        else:
            merged_II[-1][1] = max(merged_II[-1][1], r)

    ans = 0
    for l, r in merged_C:
        ans += (r - l + 1)

    prev = None
    for l, r in merged_II:
        for idx in range(l - 1, r):
            v = A[idx]
            if v == prev:
                continue
            prev = v
            if not covered(v):
                ans += 1

    print(ans)


def main():
    for _ in range(int(input())):
        solve()

main()
