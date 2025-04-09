T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    total_breaks = 0
    for stick in A:
        if stick >= 2:
            total_breaks += (stick - 1)
    print(total_breaks)
