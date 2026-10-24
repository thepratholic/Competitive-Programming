
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ranks = [tuple(map(int, input().split())) for _ in range(n)]

    cand = 0

    for i in range(1, n):
        wins = 0

        for j in range(5):
            if ranks[i][j] < ranks[cand][j]:
                wins += 1

        if wins >= 3:
            cand = i

    for i in range(n):
        if i == cand:
            continue

        wins = 0

        for j in range(5):
            if ranks[cand][j] < ranks[i][j]:
                wins += 1

        if wins < 3:
            print(-1)
            return

    print(cand + 1)

t = int(input())
for _ in range(t):
    solve()
