def solve():
    a1, a2, a4, a5 = map(int, input().split())

    ans = 0
    for c in range(-200, 201):
        ans = max(ans, (c == a1 + a2) + (c == a4 - a2) + (c == a5 - a4))

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
