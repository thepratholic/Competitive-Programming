def solve():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        a[i] = a[i] - b[i]

    a.sort()

    if abs(a[0]) <= a[1] and a[1] >= 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()