def solve():
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    print(-1 * s)

for _ in range(int(input())):
    solve()