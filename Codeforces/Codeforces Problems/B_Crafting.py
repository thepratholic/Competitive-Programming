def solve():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        if a[i] < b[i]:
            for j in range(n):
                if j == i:
                    continue
                else:
                    if a[j] >= 0:
                        a[i] += 1
                        a[j] -= 1


    for i in range(n):
        if a[i] >= b[i]:
            pass
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()