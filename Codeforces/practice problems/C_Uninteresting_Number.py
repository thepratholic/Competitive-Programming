def solve():
    string = input()

    s, two, three = 0, 0, 0

    for c in string:
        if c == '2': two += 1
        elif c == '3': three += 1

        s += int(c)

    s %= 9

    for i in range(three + 1):
        for j in range(two + 1):
            tSum = s
            tSum += (i * 6) + (j * 2)
            if tSum % 9 == 0:
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()