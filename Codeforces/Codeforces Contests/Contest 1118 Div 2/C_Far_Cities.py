import sys
from sys import stdin, stdout

input = stdin.readline

def ask(u, v, d):
    print(f"? {u} {v} {d}")
    stdout.flush()
    r = int(input())
    if r == -1:
        sys.exit(0)
    return r

def exact(u, v, lo):
    d = lo
    while True:
        r = ask(u, v, d)
        if r == 0:
            return d - 1
        d += 1

def solve():
    n = int(input())

    p, q = 1, 2
    d = exact(p, q, 1)

    for v in range(3, n + 1):
        r1 = ask(v, p, d + 1)
        if r1:
            dvp = exact(v, p, d + 2)
            r3 = ask(v, q, dvp + 1)
            if r3:
                dvq = exact(v, q, dvp + 2)
                p, d = v, dvq
            else:
                q, p, d = p, v, dvp
        else:
            r2 = ask(v, q, d + 1)
            if r2:
                dvq = exact(v, q, d + 2)
                p, d = v, dvq

    print(f"! {p} {q} {d}")
    stdout.flush()

t = int(input())
for _ in range(t):
    solve()