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
    A = LII()

    half = n // 2
    cnt = [0] * (half + 2)  

    for a in A:
        j1 = a + 1      
        j2 = n - a        
        x = j1 if j1 <= j2 else j2
        cnt[x] += 1

    for x in range(1, half + 1):
        if cnt[x] != 2:
            print(0)
            return
    if n & 1:
        if cnt[half+1] != 1:
            print(0)
            return

    MOD = 998244353
    print(pow(2, half, MOD))

def main():
    t = II()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
