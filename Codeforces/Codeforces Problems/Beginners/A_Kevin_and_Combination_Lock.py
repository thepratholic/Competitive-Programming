import math


def solve():

    x = int(input())

    if x % 33 == 0:
        print("YES")
        return
    else:
        print("NO")
        return

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
