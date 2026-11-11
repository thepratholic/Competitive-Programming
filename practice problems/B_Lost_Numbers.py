# Three Golden Rules :
# 1) Solution is Simple
# 2) Proof is Simple
# 3) Implementation is Simple

import sys
from itertools import permutations
input = sys.stdin.readline

def ask(i, j):
    print("?", i, j, flush=True)
    s = input().strip()
    return int(s)

def solve():
    ans = [4, 8, 15, 16, 23, 42]

    o = [-1] * 4
    for i in range(4):
        o[i] = ask(i + 1, i + 2)

    for perm in permutations(ans):
        ok = True
        for i in range(4):
            if perm[i] * perm[i + 1] != o[i]:
                ok = False
                break

        if ok:
            print("!", *perm, flush=True)
            return

solve()
