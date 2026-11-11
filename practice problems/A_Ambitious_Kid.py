def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mini = float('inf')
    for i in range(n):
        mini = min(mini, abs(a[i]))

    print(mini)

if __name__ == "__main__":
    solve()