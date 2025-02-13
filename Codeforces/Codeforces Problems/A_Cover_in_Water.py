for _ in range(int(input())):
    
    n = int(input())
    s = input()
    count = 0
    continuous_three_empty_cells = False
    for i in range(n):
        if s[i] == '.' and i+1 < n and s[i+1] == '.' and i+2 < n and s[i+2] == '.':
            continuous_three_empty_cells = True
            break
        if s[i] == '.':
            count += 1

    if continuous_three_empty_cells:
        print(2)
    else:
        print(count)