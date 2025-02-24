import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, l = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()
    first, last = a[0] - 0, l - a[-1]

    maxi = float('-inf')

    for i in range(n - 1):
        maxi = max(maxi, a[i+1] - a[i])

    result = max(first, last, maxi / 2)

    # Ensure precision of at least 10^-9
    print(f"{result:.10f}")

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
    solve()

if __name__ == "__main__":
    main()