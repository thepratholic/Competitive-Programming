def solve():

    x, y = map(int, input().split())

    if x - y == 1:
        print("NO")
        return
    else: print("YES")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()