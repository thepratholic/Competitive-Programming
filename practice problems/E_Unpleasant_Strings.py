
import sys
from array import array

sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    q = int(input())
    queries = [input().strip() for _ in range(q)]

    NOT_FOUND = n + 1
    nxt = array('i', [NOT_FOUND]) * ((n + 2) * k)

    for i in range(n - 1, -1, -1):
        cur = i * k
        nex = (i + 1) * k

        for c in range(k):
            nxt[cur + c] = nxt[nex + c]

        c = ord(s[i]) - ord('a')
        nxt[cur + c] = i + 1

    dp = [0] * (n + 2)

    for i in range(n, -1, -1):
        ans = n + 1
        cur = i * k

        for c in range(k):
            pos = nxt[cur + c]

            if pos == NOT_FOUND:
                ans = 1
                break

            ans = min(ans, 1 + dp[pos])

        dp[i] = ans

    for t in queries:
        pos = 0

        for ch in t:
            c = ord(ch) - ord('a')
            pos = nxt[pos * k + c]

            if pos == NOT_FOUND:
                break

        if pos == NOT_FOUND:
            print(0)
        else:
            print(dp[pos])

t = 1
for _ in range(t):
    solve()
