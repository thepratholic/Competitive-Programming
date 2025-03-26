def solve():
    n = int(input())

    a = list(map(int, input().split()))

    bhoomi =  n - 1

    ans = 0

    for i in range(n):
        if a[i] >= a[bhoomi]:
            ans += (bhoomi - i)
            break

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()