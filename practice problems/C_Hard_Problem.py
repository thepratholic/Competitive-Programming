def solve():
    m, a, b, c = map(int, input().split())

    ans, rem = 0, 0

    ans += min(m, a)
    rem += (m - min(m, a))

    ans += min(m, b)
    rem += (m - min(m, b))

    ans += min(rem, c)

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()