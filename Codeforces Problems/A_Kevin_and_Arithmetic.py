def solve():
    n = int(input())

    a = list(map(int, input().split()))
    a.sort(key=lambda x : x % 2)
    s = 0
    points = 0
    for i in range(n):
        s += a[i]
        if s % 2 == 0:
            points += 1

        while s % 2 != 1:
            s //= 2

    print(points)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()