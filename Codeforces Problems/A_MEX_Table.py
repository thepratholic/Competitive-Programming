def solve():
    n, m = map(int, input().split())

    print(max(n, m) + 1)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()