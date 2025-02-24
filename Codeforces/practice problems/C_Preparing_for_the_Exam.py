def solve():
    n, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    q = list(map(int, input().split()))

    ans = [0] * m

    if k == n:
        for i in range(m):
            ans[i] = 1

    elif k == n - 1:
        list_num = 1
        for i in q:
            if list_num == i:
                list_num += 1

        for i in range(m):
            if a[i] == list_num:
                ans[i] = 1


    for i in ans:
        print(i, end="")
    print()

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
