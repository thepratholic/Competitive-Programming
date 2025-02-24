def solve():

    n, k = map(int, input().split())

    l = []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            l.append(i)
            n //= i
    if n > 1:
        l.append(n)

    if len(l) < k:
        print(-1)
        return

    while len(l) > k:
        x = l.pop()
        l[-1] *= x

    print(*l)

if __name__ == "__main__":
    solve()