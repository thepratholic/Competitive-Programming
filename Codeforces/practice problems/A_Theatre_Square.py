import sys
from math import ceil

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, m, a = map(int, input().split())


    r, c = ceil(n/a), ceil(m/a)
    print(r * c)

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()