def mex(arr):
    s = set(arr)
    i = 0
    while i in s:
        i += 1
    return i

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    operations = []
    
    while len(a) > 1:
        found = False
        
        for i in range(len(a) - 1):
            if mex([a[i], a[i+1]]) == 0:
                operations.append((i+1, i+2))
                a = a[:i] + [0] + a[i+2:]
                found = True
                break
        
        if not found:
            operations.append((len(a)-1, len(a)))
            a = a[:-2] + [mex([a[-2], a[-1]])]
    
    print(len(operations))
    for l, r in operations:
        print(l, r)