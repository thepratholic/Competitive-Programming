# cook your dish here
for _ in range(int(input())):
    
    m, k = map(int, input().split())
    
    s = input()
    
    swishes = s.count('S')
    
    if swishes >= k:
        print(m) 
    else:
        remaining_needed = k - swishes
        max_possible_remaining = m  
        print(max(m, remaining_needed + m - 1))
    