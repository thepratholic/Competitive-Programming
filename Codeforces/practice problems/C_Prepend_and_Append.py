def solve():
    n = int(input())

    s = input().strip()

    if n == 1:
        print(1)
        return
    

    while len(s) >= 2 and s[0] != s[-1]:
        s = s[1:-1]

    print(len(s))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
