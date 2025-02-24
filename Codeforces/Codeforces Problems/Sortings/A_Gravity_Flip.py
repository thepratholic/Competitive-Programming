import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    print(*a)

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()