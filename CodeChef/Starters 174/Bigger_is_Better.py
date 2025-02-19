def solve():
    n = int(input())

    a = input()

    ans = ""

    for i in range(n):
        ans += "z"

    print(ans if ans > a else "-1")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()