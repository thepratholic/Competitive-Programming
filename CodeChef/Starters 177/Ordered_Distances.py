def find_pivot_index(x, y):
    n = len(x)
    
    for i in range(n):
        pivot = x[i]
        

        pairs = [(abs(x[j] - pivot), x[j]) for j in range(n)]
        
        pairs.sort()
        
 
        expected_y = [pair[1] for pair in pairs]
        
        if expected_y == y:
     
            return i + 1
    

    return -1


t = int(input())

for _ in range(t):
    n = int(input())
    
    x = list(map(int, input().split()))
    

    y = list(map(int, input().split()))
    

    result = find_pivot_index(x, y)
    

    print(result)