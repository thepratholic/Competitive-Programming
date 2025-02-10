def solve():

    n = int(input())
    a = list(map(int, input().split()))

    ans = "NO"

    for i in range(n - 1):
        if 2 * min(a[i], a[i+1]) > max(a[i], a[i+1]):
            ans = "YES"

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()