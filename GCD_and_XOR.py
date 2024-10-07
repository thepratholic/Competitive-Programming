# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))

    cnt = 0
    for x in ar:
        if x == k:
            cnt += 1
    if cnt == n:
        print(0)

    else:
        start = end = -1

        for i in range(n):
            if ar[i] != k:
                if start == -1:
                    start = i

                end = i
        gcd = xor = True

        for i in range(start, end+1):
            if ar[i] % k != 0:
                gcd = False

            if ar[i] ^ k != ar[start] ^ k:
                xor = False

        if xor or gcd:
            print(1)
        else: print(2)
