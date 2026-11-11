t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    if s < s[::-1]:
        print("YES")
        continue
    
    if k == 0:
        print("NO")
        continue
    
    found = False
    for i in range(n):
        for j in range(i+1, n):
            s_chars = list(s)
            s_chars[i], s_chars[j] = s_chars[j], s_chars[i]
            new_s = ''.join(s_chars)
            
            if new_s < new_s[::-1]:
                found = True
                break
        
        if found:
            break
    
    print("YES" if found else "NO")