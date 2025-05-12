T = int(input())
for _ in range(T):
    n= int(input())
    a = list(map(int, input().split()))
    inv = 0  
    count = 0      
    l = 1       
    res = []
    for i in range(n):
        if a[i] == 1:
            inv += l
            count+= l
            l += 1
        else:
            inv = 2 * inv + count
            count *= 4
            l *= 2
        res.append(inv)
    print(*res)