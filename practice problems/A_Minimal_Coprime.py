def solve():
    l, r = map(int, input().split())

    ans = r - l
    if l == 1 and r == 1:
        print(1)
        return
    else:
        print(ans)
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()