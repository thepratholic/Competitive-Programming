# cook your dish here
for _ in range(int(input())):

    x, y = map(int, input().split())

    if y >= (x / 2):
        print("YES")

    else:
        print("NO")