import math
def solve():
    n = int(input())
    s = input()

    cnthyphen = 0
    cntunderscore = 0

    for i in s:
        if i == "-":
            cnthyphen += 1
        else:
            cntunderscore += 1

    left = math.floor(cnthyphen / 2)
    right = math.ceil(cnthyphen / 2)

    print(cntunderscore * left * right)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()