def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        a = [0] * n
        
        for i in range(n):
            if i == 0:
                diff = b[0]
            else:
                diff = b[i] - b[i-1]
            
            last_pos = (i + 1) - diff
            
            if last_pos == 0:
                a[i] = i + 1
            else:
                a[i] = a[last_pos - 1]
        
        print(*a)

solve()