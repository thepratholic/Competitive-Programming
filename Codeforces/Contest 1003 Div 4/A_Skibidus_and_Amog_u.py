def solve():
    w = input()


    ans = ""
    if len(w) == 2:
        print("i")
        return

    for i in range(len(w) - 3, -1, -1):
        ans += w[i]
    ans = ans[::-1]
    ans += "i"

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

