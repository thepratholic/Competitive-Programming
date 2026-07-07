import sys

input = sys.stdin.readline

def solve():
    a = input().strip()
    b = input().strip()

    prea = []
    s = 0
    for ch in a:
        s = (s + int(ch)) % 10
        prea.append(s)

    preb = []
    s = 0
    for ch in b:
        s = (s + int(ch)) % 10
        preb.append(s)

    if prea[-1] != preb[-1]:
        print(-1)
        return

    n = len(prea)
    m = len(preb)

    prev = [0] * m

    for i in range(1, n):
        cur = [0] * m
        for j in range(1, m):
            if prea[i - 1] == preb[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur

    print(prev[m - 1] + 1)


t = int(input())
for _ in range(t):
    solve()