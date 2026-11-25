def good(x):
    return bin(x).count('1') % 2 == 0


def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    answer = sum(good(x) for x in a)
    ans = [str(answer)]

    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1

        answer -= good(a[p])
        a[p] = x
        answer += good(a[p])

        ans.append(str(answer))

    print(*ans)


t = int(input())
for _ in range(t):
    solve()