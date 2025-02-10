def solve():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_diff = 0

    for i in range(n - 1):
        if a[i] > b[i+1]:
            max_diff += (a[i] - b[i+1])

    max_diff += a[n-1]

    print(max_diff)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()