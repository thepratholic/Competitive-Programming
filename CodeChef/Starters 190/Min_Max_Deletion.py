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


#@bootstrap
def solve():
    global_index = 0
    data = sys.stdin.read().split()
    T = int(data[global_index])
    global_index += 1
    out = []

    for _ in range(T):
        N = int(data[global_index])
        Q = int(data[global_index + 1])
        global_index += 2

        A = list(map(int, data[global_index:global_index + N]))
        global_index += N

        score = 0
        for i in range(N - 1):
            score += min(A[i], A[i + 1])

        for _ in range(Q):
            i = int(data[global_index]) - 1
            x = int(data[global_index + 1])
            global_index += 2

            if i > 0:
                score -= min(A[i], A[i - 1])
            if i < N - 1:
                score -= min(A[i], A[i + 1])

            A[i] = x 

            if i > 0:
                score += min(A[i], A[i - 1])
            if i < N - 1:
                score += min(A[i], A[i + 1])

            out.append(str(score))

    print('\n'.join(out))


def main():
    # for _ in range(II()):
        solve()
main()