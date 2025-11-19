t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    c1 = arr.count(1)
    c2 = arr.count(2)
    c3 = arr.count(3)
    
    keep1 = c1 + min(c2, 1)
    keep3 = c3 + min(c2, 1)
    keep2 = min(c2, 1)
    
    max_keep = max(keep1, keep3, keep2)
    print(n - max_keep)
