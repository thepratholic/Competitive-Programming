for _ in range(int(input())):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    copy_a = sorted(arr)

    if copy_a == arr or k > 1:
        print("YES")
    else:
        print("NO")