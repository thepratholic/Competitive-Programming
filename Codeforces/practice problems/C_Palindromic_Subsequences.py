import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n = int(input())
    v = [0] * n

    if n == 6:
        print("1 1 2 3 1 2")
        return
    elif n == 7:
        print("1 1 2 3 1 2 2")
        return

    for i in range(n // 2):
        v[i] = i + 1

    for i in range(n // 2, n):
        v[i] = i - n // 2 + 1

    print(" ".join(map(str, v)))

def main():
    t = 1
    t = int(inp())  # Uncomment if multiple test cases exist
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()