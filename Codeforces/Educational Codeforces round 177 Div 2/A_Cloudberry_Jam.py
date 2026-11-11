def solve():
    n = int(input())

    ans = ((n * 2) + (n * 2) * 3) // 4

    print(n * 2)
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()