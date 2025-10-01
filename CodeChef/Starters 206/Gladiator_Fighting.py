t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 2:
        print(0, 0)
    else:
        s_min = n - 2
    
        s_max = (n - 1) * (n - 2) // 2

        print(s_min, s_max)