import sys,heapq
from collections import Counter
input=sys.stdin.readline

def solve():
    n=int(input().strip())
    a=list(map(int,input().split()))
    c=Counter(a)
    h=[-x for x in c.keys()]
    heapq.heapify(h)
    ans=[]
    s=0
    while len(ans)<n and h:
        x=-heapq.heappop(h)
        if x!=s:
            ans.append(x); s+=x; c[x]-=1
            if c[x]>0: heapq.heappush(h,-x)
        else:
            if not h:
                ans.append(x); s+=x; c[x]-=1
                if c[x]>0: heapq.heappush(h,-x)
            else:
                y=-heapq.heappop(h)
                ans.append(y); s+=y; c[y]-=1
                if c[y]>0: heapq.heappush(h,-y)
                heapq.heappush(h,-x)
    for v,cnt in c.items():
        while cnt>0:
            ans.append(v); cnt-=1
            c[v]-=1
    print(*ans)

t=int(input().strip())
for _ in range(t): solve()
