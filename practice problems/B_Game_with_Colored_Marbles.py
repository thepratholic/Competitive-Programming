from collections import defaultdict


def solve():

    n = int(input())

    a = list(map(int, input().split()))

    mpp = defaultdict(int)

    for x in a:
        mpp[x] += 1


    exactly1, morethan1 = 0, 0
    for k, v in mpp.items():
        if v > 1:
            morethan1 += 1

        if v == 1:
            exactly1 += 1

    print(morethan1 + (exactly1 + 1) // 2 * 2)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()