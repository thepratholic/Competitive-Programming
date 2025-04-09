def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input()
        bal = 0
        ans = 0
        for c in s:
            if c == '0':
                bal += 1
            else:
                bal -= 1
            if bal == 0:
                ans += 1
        print(1 << ans)

solve()