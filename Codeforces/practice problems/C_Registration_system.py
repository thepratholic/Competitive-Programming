from collections import defaultdict

def solve():
    n = int(input())
    mpp = defaultdict(int)

    for _ in range(n):

        s = input()

        if s not in mpp:
            mpp[s] += 1
            print("OK")

        else:
            print(s, mpp[s], sep="")
            mpp[s]+=1

solve()