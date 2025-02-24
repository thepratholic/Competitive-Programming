import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    s, n = map(int,input().split())

    dragons = [tuple(map(int, input().split())) for _ in range(n)]

    dragons.sort()

    for xi, yi in dragons:
        if s <= xi:
            print("NO")
            return
        s += yi
    print("YES")

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
    solve()

if __name__ == "__main__":
    main()