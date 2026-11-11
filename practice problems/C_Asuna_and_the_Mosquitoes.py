def solve():
    n = int(input())

    a = list(map(int, input().split()))

    s = sum(a)

    odds = sum(1 for i in range(n) if a[i] % 2 == 1)
    evens = n - odds

    
    if odds == 0 or evens == 0:
        print(max(a))
        return
    
    print(s - (odds - 1))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()