def solve():
    n = int(input())
    a = list(map(int, input().split()))

    sqs = set()
    k = 1
    while k * k <= 100 * 1000:
        sqs.add(k * k)
        k += 2

    ans = 0
    cur = 0
    for t in a:
        cur += t
        if cur in sqs:
            ans += 1


    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()