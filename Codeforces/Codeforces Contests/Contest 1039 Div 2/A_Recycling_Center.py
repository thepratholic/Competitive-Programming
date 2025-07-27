t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    
    coins = 0
    dl = []
    
    for x in a:
        if x > c:
            coins += 1
        else:
            v = c // x
            d = 0
            while (1 << (d + 1)) <= v:
                d += 1
            dl.append(d)
    
    dl.sort()
    t = 0
    freeOK = 0
    
    for d in dl:
        if t <= d:
            freeOK += 1
            t += 1
    
    coins += len(dl) - freeOK
    print(coins)