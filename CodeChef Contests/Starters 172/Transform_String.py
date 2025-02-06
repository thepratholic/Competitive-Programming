# cook your dish here
for _ in range(int(input())):
    
    a = input()
    b = input()
    
    n, m = len(a), len(b)
    
    ptr = m - 1
    ans = 0
    for i in range(n-1, -1, -1):
        if ptr >= 0 and b[ptr] == a[i]:
            ptr -= 1 
        else:
            ans += (ptr + 2)
            
    if ptr >= 0:
        print(-1)
    else:
        print(ans)