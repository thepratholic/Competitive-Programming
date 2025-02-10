def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = []

    ans.append(a[0])

    for i in range(1, n):
        if a[i] >= a[i-1]:
            ans.append(a[i])
        else:
            ans.append(a[i])
            ans.append(a[i])

    print(len(ans))
    print()
    for i in ans:
        print(i, end=" ")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()