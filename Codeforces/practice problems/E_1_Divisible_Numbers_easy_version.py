from math import gcd

def solve():
    # write per-test-case logic here
    a, b, c, d = map(int, input().split())

    fl = 0
    for i in range(a + 1, c + 1):
        num = a * b // gcd(a * b, i)

        num = (d // num) * num

        if num > b and num <= d:
            print(i, num)
            fl = 1
            break

    if fl == 0:
        print(-1, -1)
        

t = int(input())
for _ in range(t):
    solve()