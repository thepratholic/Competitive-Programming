def solve():
    n = int(input())

    a = sorted(list(map(int, input().split())))

    legs = 0
    for i in range(n - 1, 0, -1):
        if a[i - 1] == a[i]:
            legs = a[i] * 2
            del a[i]
            del a[i - 1]
            break

    
    for i in range(1, len(a)):
        if a[i] - a[i - 1] < legs:
            print(legs // 2, legs // 2, a[i - 1], a[i])
            break
    else:
        print(-1)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()