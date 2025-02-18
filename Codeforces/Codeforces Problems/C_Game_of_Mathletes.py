def solve():

    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    a.sort()

    l, r = 0, n - 1
    score = 0
    while l < r:
        s = a[l] + a[r]

        if s < k:
            l += 1

        elif s > k:
            r -= 1

        else:
            score += 1
            l += 1
            r -= 1

    print(score)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()