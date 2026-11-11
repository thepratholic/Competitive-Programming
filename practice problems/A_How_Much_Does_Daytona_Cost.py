def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print("YES") if a[0] == k else print("NO")
        return
    
    for i in range(n):
        if a[i] == k:
            print("YES")
            return
    print("NO")

for _ in range(int(input())):
    solve()