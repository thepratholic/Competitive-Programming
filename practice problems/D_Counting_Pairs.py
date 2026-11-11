import bisect
def solve():
    n, x, y = map(int, input().split())

    a = sorted(list(map(int, input().split())))

    total_sum = sum(a)
    lb = total_sum - y
    ub = total_sum - x
    cnt = 0
    for i in range(n):
        lower = bisect.bisect_left(a, lb - a[i], i + 1)
        upper = bisect.bisect_right(a, ub - a[i], i + 1)

        cnt += upper - lower

    print(cnt)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()