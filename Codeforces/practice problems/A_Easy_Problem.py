def solve():
    n = int(input())

    pairs = []

    for i in range(1, n+1):
        s = i + (n - i)
        if s == n:
            pairs.append((i, n - i))

    print(len(pairs) - 1)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()