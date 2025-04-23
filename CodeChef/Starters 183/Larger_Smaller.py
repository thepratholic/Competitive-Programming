import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    mn, mx = min(A), max(A)
    print(max(0, mx - mn - 1))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
