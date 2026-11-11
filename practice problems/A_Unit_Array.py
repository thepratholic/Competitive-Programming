def solve():
    n = int(input())
    a = list(map(int, input().split()))

    negOnes, posOnes = 0, 0

    for i in a:
        if i == 1:
            posOnes += 1
        else:
            negOnes += 1

    ans = 0
    while negOnes > posOnes or negOnes % 2 == 1:
        ans += 1
        negOnes -= 1
        posOnes += 1

    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()