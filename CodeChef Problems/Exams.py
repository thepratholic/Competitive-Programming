# cook your dish here
for _ in range(int(input())):

    x, y, z = map(int, input().split())

    total = x * y

    avg = total // 2

    if z > avg:
        print("YES")
    else:
        print("NO")