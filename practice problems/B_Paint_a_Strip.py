
def solve():
    n = int(input())

    ans, cur = 1, 1

    while True:
        if cur >= n:
            print(ans)
            return
        ans += 1
        cur = cur * 2 + 2


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()