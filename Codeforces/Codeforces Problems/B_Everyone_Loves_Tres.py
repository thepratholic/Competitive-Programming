def solve():
    n = int(input())

    if n == 1 or n == 3:
        print(-1)
        return
    
    if n == 2:
        print(66)
        return
    ans = ""
    if n % 2 == 0:
        for i in range(n-2):
            ans += "3"

        ans += "66"
        print(ans)
        return
    
    if n % 2 == 1:
        for i in range(n - 4):
            ans += "3"

        ans += "6366"
        print(ans)
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()