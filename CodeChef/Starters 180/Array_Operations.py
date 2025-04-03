def solve():
    n = int(input())

    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return
    
    ans = -1

    for i in range(n):
        l, r = i, n - i - 1

        ans = max(ans, a[i] + l // 2 + r // 2)

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()