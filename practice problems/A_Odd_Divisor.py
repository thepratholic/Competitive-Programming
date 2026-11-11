def solve():
    n = int(input())

    while n % 2 == 0:
        n //= 2
    
    if n == 1:
        print("NO")
    else: print("YES")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()