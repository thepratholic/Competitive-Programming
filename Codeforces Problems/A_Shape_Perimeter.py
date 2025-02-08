def solve():
    n, m = map(int, input().split())

    x, y = [0] * n, [0] * n

    for i in range(n):
        x[i], y[i] = map(int, input().split())

    ans = 2 * (sum(x) + m - x[0] + sum(y) + m - y[0])
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()