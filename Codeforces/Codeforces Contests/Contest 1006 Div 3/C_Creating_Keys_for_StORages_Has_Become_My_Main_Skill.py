def solve():

    n, x = map(int, input().split())

    v = [x] * n

    for i in range(n):
        if i | x == x:
            v[i] = i

    orr = 0

    for i in v:
        orr |= i

    if orr != x:
        v[-1] = x

    print(*v)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()