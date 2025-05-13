import sys
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    d = [0, 0]
    for _ in range(n):
        s, e = map(int, input().split())
        d[s-1] = max(d[s-1], e)

    INF = 10**30
    ans = INF

    if d[0] > 0:
        cnt1 = (h + d[0] - 1) // d[0]
        ans = min(ans, cnt1)

    if d[1] > 0:
        cnt2 = (h + d[1] - 1) // d[1]
        ans = min(ans, 2 * cnt2)

    if d[1] > 0 and d[0] > 0:
        k = h // d[1]
        rem = h - k * d[1]
        if 0 < rem <= d[0]:
            ans = min(ans, 2 * k + 1)

    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
