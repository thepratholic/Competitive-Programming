def solve():
    n, k = map(int, input().split())

    if n % k != 0:
        print(1)
        print(n)
        return
    else:
        print(2)
        print(1, n - 1)
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()