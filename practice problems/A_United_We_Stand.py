def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    b, c = [a[0]], []

    for i in range(1, n):
        if(b[-1] >= a[i]):
            b.append(a[i])
        else:
            c.append(a[i])

    if not b or not c:
        print(-1)
        return

    print(len(b), len(c))
    print(*b)
    print(*c)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()