import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    total = 0
    for i in range(n - 1):
        total += abs(a[i] - a[i + 1])

    mg = 0

    mg = max(mg, abs(a[0] - a[1]))

    mg = max(mg, abs(a[n - 2] - a[n - 1]))

    for i in range(1, n - 1):
        gain = abs(a[i - 1] - a[i]) + abs(a[i] - a[i + 1]) - abs(a[i - 1] - a[i + 1])
        mg = max(mg, gain)

    print(total - mg)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
