def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mini_changes = float("inf")
    if a != sorted(a):
        print(0)
        return
    else:
        for i in range(1, n):
            mini_changes = min(mini_changes, a[i] - a[i-1])

        print((mini_changes // 2) + 1)
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()