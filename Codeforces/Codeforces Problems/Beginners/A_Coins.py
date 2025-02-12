def solve():
    n, k = map(int, input().split())

    if n % 2 == 0:
        print("YES")

    else:
        if k % 2 == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()