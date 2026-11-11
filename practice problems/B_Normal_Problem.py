def solve():
    s = input()

    ans = ""

    for i in reversed(s):
        if i == "q":
            ans += "p"
        elif i == "p":
            ans += "q"

        else:
            ans += "w"

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()