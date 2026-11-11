def solve():
    n = int(input())
    a = list(map(int, input().split()))

    tar = {0: 3, 1: 1, 3: 1, 2: 2, 5: 1} 
    cnt = {0: 0, 1: 0, 3: 0, 2: 0, 5: 0} 
    
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        
        if all(cnt[d] >= tar[d] for d in tar):
            print(i + 1)
            return
    
    print(0)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
