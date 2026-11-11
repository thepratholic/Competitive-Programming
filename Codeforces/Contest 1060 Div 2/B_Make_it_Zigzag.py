def solve():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        c=0
        mx=0
        for i in range(n):
            mx=max(mx,a[i])
            if i&1: a[i]=mx
            if i:
                if i&1:
                    if a[i-1]>=a[i]:
                        d=a[i-1]-a[i]+1
                        c+=d;a[i-1]-=d
                else:
                    if a[i-1]<=a[i]:
                        d=a[i]-a[i-1]+1
                        c+=d;a[i]-=d
        print(c)
solve()
