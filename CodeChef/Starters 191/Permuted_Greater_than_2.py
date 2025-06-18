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

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve():
    X, Y, Z = MII()

    if X == 0:
        print("Yes")
    elif Z == 0:
        if X >= 2 or Y >= 1:
            print("No")
        else:
            print("Yes")
    else:
        if Z >= (X - 1):
            print("Yes")
        else:
            print("No")




def main():
    for _ in range(II()):
        solve()
main()