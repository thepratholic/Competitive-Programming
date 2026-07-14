MOD = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = []
    cnt_minus = 0

    i = 0
    while i < n:
        val = a[i]
        cnt = 0

        while i < n and a[i] == val:
            cnt += 1
            i += 1

        freq.append((val, cnt))

        if val == -1:
            cnt_minus = cnt

    even = 1
    for val, cnt in freq:
        even = (even * pow(2, cnt - 1, MOD)) % MOD

    ans = even

    if cnt_minus == 0:
        print(ans)
        return

    for i in range(1, len(freq)):
        if freq[i - 1][0] + 1 == freq[i][0]:
            ans = (ans + even) % MOD

    print(ans)


t = int(input())
for _ in range(t):
    solve()