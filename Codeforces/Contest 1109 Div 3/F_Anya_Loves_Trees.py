import sys
from sys import stdin

input = stdin.readline

def solve():
    n = int(input())

    parent = [0] + list(map(int, input().split()))
    nums = [0] + list(map(int, input().split()))

    childs = [[] for _ in range(n + 1)]

    for i in range(2, n + 1):
        childs[parent[i - 1]].append(i)

    order = []
    q = [1]
    head = 0

    while head < len(q):
        v = q[head]
        head += 1
        order.append(v)
        q.extend(childs[v])

    mn = [0] * (n + 1)
    mx = [0] * (n + 1)
    sz = [0] * (n + 1)
    ok = [True] * (n + 1)

    order.reverse()

    for v in order:

        if not childs[v]: # yeh leaf node hai
            mn[v] = mx[v] = nums[v]
            sz[v] = 1
            continue

        good = True
        total = 0
        lo = 10 ** 18
        hi = -1

        mins = []

        for c in childs[v]:

            if not ok[c]:
                good = False

            total += sz[c]
            lo = min(lo, mn[c])
            hi = max(hi, mx[c])

            mins.append(mn[c])

        if hi - lo + 1 != total:
            good = False

        if good:
            m = len(childs[v])

            order_idx = sorted(range(m), key=lambda i: mins[i])

            rank = [0] * m

            for r, idx in enumerate(order_idx):
                rank[idx] = r

            start = rank[0]

            for i in range(m):
                if rank[i] != (start + i) % m:
                    good = False
                    break

        mn[v] = lo
        mx[v] = hi
        sz[v] = total
        ok[v] = good

    print("YES" if ok[1] else "NO")


t = int(input())
for _ in range(t):
    solve()