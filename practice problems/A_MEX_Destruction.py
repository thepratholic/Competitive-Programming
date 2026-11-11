def solve():
    n = int(input())
    a = input().split(" 0")

    a1 = []
    for i in a:
        if i != "0" and i:
            a1.append(i)

    print(min(2, len(a1)))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()