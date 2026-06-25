
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):

        for j in range(i + 1, n):
            if a[j] > a[i]:
                a[j] = a[i]
                break

    print(sum(a))

t = int(input())
for _ in range(t):
    solve()