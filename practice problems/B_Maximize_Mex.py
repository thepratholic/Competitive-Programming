for _ in range(int(input())):
    n, x = map(int, input().split())
    a = [int(y) for y in input().split()]
    
    freq = [0] * (n + 2)
    
    for i in a:
        if i < n + 2:
            freq[i] += 1
    
    for i in range(n + 2):
        if freq[i] == 0:
            print(i)
            break
        elif freq[i] > 1:
            if i + x < n + 2:
                freq[i + x] += (freq[i] - 1)
