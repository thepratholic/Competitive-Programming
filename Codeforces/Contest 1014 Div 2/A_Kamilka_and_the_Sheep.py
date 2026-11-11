def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        max_pleasure = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = abs(a[i] - a[j])
                max_pleasure = max(max_pleasure, diff)
        
        print(max_pleasure)

if __name__ == "__main__":
    solve()