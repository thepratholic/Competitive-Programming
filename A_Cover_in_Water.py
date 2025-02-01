for _ in range(int(input())):
    
    n = int(input())
    s = input()
    count = 0
    for i in range(1, n-1):
        if s[i] == '.' and s[i-1] == '.' and s[i+1] == '.':
                count += 2
        elif s[i] == '.':
            count += 1

    print(count)