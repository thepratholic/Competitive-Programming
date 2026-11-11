def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 2:
        if a[0] % 2 == a[1] % 2:
            print("YES")
            return
        else:
            print("NO")
            return

    blues, reds = 0, 0
    for i in range(n):
        if a[i] % 2 == 1:
            blues += a[i]
        else:
            reds += a[i]

    if (blues % 2) == (reds % 2):
        print("YES")
        return
    else:
        print("NO")
        return
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()