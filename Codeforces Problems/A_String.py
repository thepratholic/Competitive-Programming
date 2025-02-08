def solve():
    s = input()

    changes = 0

    for i in s:
        if i == "1":
            changes += 1

    print(changes)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()