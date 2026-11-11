import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def powm(x, n):
    res = 1
    x %= MOD
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res

def solve():
    n, k = map(int, input().split())

    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v, x = map(int, input().split())
        if x == 0:
            adj[u].append(v)
            adj[v].append(u)

    vis = [False] * (n + 1)

    def dfs(start):
        stack = [start]
        vis[start] = True
        sz = 0

        while stack:
            u = stack.pop()
            sz += 1
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    stack.append(v)
        return sz

    bad = 0
    for i in range(1, n + 1):
        if not vis[i]:
            sz = dfs(i)
            bad = (bad + powm(sz, k)) % MOD

    ans = (powm(n, k) - bad) % MOD
    print(ans)

solve()