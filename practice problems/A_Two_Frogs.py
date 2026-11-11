def solve():
    n, a, b = map(int, input().split())

    if (a ^ b) & 1:
        print("NO")
        return
    else:
        print("YES")
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
