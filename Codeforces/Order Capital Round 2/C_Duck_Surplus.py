def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0

    for x in a:
        if ans > x:
            ans += x

        else:
            ans = x

    print(ans)


t = int(input())
for _ in range(t):
    solve()
