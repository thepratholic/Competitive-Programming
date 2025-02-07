def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = [-1] * n 

    for i in range(n):
        b[i] = (n + 1) - a[i]

    print(*b)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()