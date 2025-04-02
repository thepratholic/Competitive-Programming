# cook your dish here
# Solution for Maximum Ones problem

def solve_max_ones(s, k):
    n = len(s)
    s = list(map(int, s))
    
    result = s.copy()
    operations_left = k
    
    for i in range(n-2, -1, -1):
        if operations_left > 0 and result[i] == 0 and result[i+1] == 1:
            result[i] = 1 
            operations_left -= 1
    
    return sum(result) 

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    s = input().strip()
    
    print(solve_max_ones(s, k))