T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    d = max(X, Y)
    p = min(X, Y)
    
    op = max(0, p - (d // 2))
    ap = max(0, 2 * p - d)
    
    print(min(ap, op))
