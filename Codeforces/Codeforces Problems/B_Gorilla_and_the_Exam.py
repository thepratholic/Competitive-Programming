from collections import Counter
def solve():
    n,k=map(int,input().split())
    freq=Counter(input().split())
    m=len(freq)
    for el in sorted(freq.values()) :
       if k<el:
           break
       k-=el
       m-=1
    print(max(1,m))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()