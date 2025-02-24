import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, m = map(int, input().split())

    a = sorted(list(map(int, input().split())))

    maxi = 0
    s = 0
    for i in range(m):
        if a[i] < 0:
             s += (-1 * a[i])
             maxi = max(maxi, s)

        else: break
    print(maxi)

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()