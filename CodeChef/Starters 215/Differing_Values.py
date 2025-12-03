import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    ones = s.count('1')

    vis = [0]*n
    chains = []

    for i in range(n):
        if not vis[i]:
            c = 0
            j = i
            while j < n:
                vis[j] = 1
                c += 1
                j += k
            chains.append(c)

    mn = 0
    mx = 0
    for c in chains:
        mn += c // 2
        mx += (c + 1) // 2

    print("YES" if mn <= ones <= mx else "NO")


t = int(input())
for _ in range(t):
    solve()
