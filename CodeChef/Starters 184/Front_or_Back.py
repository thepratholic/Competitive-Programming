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

def I():   return input()
def II():  return int(input())
def MII(): return map(int, input().split())
def LI():  return list(input().split())
def LII(): return list(map(int, input().split()))
def GMI(): return map(lambda x: int(x)-1, input().split())
def LGMI():return list(map(lambda x: int(x)-1, input().split()))
def WRITE(out):     return print('\n'.join(map(str, out)))
def WS(out):        return print(' '.join(map(str, out)))
def WNS(out):       return print(''.join(map(str, out)))
def WSNOPRINT(out): return ''.join(map(str, out))

def solve():
    n = II()
    a = LII()

    cnt = [0] * n

    for i in range(n):
        cnt[a[i]] += 1

    ans = 1
    MOD = 998244353
    for i in range(n // 2):
        if cnt[i] + cnt[n - i - 1] != 2:
            print(0)
            return
        ans = (ans * 2) % MOD

    print(ans)


def main():
    t = II()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
