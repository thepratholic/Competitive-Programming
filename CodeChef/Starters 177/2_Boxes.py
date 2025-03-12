def min_time_to_achieve_difference(x, y, k):
    initial_diff = abs(x - y)
    
    target_diff = k
    
    diff_to_achieve = abs(initial_diff - target_diff)
    
    if diff_to_achieve % 2 == 1:
        return -1
    
    return diff_to_achieve // 2

t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())
    
    result = min_time_to_achieve_difference(x, y, k)
    print(result)