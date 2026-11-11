n=int(input())
a=list(map(int,input().split()))
cnt1=0
for x in a:
    if x==1:cnt1+=1
mx=-10**18
cursum=0
for i in range(n):
    if a[i]==0:
        a[i]=1
    else:
        a[i]=-1
for x in a:
    cursum=max(x,cursum+x)
    mx=max(mx,cursum)
print(mx+cnt1)