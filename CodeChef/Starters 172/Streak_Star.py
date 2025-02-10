for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    max_streak = 1 
    for i in range(n):
        modified = a[:] 
        modified[i] *= x 

        current_streak = 1
        for j in range(1, n):
            if modified[j] >= modified[j-1]:
                current_streak += 1
            else:
                current_streak = 1  # Reset streak
            
            max_streak = max(max_streak, current_streak)
            
    print(max_streak)