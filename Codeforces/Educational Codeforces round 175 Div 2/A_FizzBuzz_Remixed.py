def solve():
    # MOD = 1e9
    n = int(input())
    if n == 0:
        print(1)
        return
    print(3 * (n // 15) + min(3, (n % 15) + 1))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()