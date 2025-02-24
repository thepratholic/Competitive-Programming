def solve():
    n = int(input())

    a = list(map(int, input().split()))

    a.sort()

    print(*a)

if __name__ == "__main__":
    solve()