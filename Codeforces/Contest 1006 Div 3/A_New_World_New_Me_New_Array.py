from math import ceil
def solve():
    n, k, p = map(int, input().split())

    if k == 0:
        print(0)
        return

    ans = ceil(abs(k) / p)

    if ans <= n:
        print(ans)
        return
    else:
        print(-1)
        return


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()