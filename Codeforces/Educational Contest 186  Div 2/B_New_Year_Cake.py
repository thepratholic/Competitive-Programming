import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())

    white, dark = a, b
    w1 = d1 = 0  
    w2 = d2 = 0   

    ans = 0

    for i in range(60):
        size = 1 << i

        if i % 2 == 0:
            w1 += size
            d2 += size
        else:
            d1 += size
            w2 += size

        ok1 = (w1 <= white and d1 <= dark)
        ok2 = (w2 <= white and d2 <= dark)

        if ok1 or ok2:
            ans = i + 1
        else:
            break

    print(ans)

t = int(input())
for _ in range(t):
    solve()
