for t in range(int(input())):

    n=int(input())
    m=[0]*(2*n)
    
    for i in range(n):
        a=list(map(int,input().split()))
        for j in range(n):
            if(a[j]<0):
                m[n-i+j]=max(m[n-i+j],abs(a[j]))
    print(sum(m))

