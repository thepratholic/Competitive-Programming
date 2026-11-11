def solve():
    a = input().strip()
    b = input().strip()

    n, m = len(a), len(b)
    ans = n + m
    for i in range(m):
        j = i

        for c in a:
            if j < m and c == b[j]:
                j += 1

        ans = min(ans, n + m - (j - i))

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()