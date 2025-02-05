for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if c % 2 == 0:
        if a > b:
            print("First")
        else:
            print("Second")

    else:
        if b > a:
            print("Second")
        else:
            print("First")