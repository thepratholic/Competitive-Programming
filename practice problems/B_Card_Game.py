import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def f(a, b):
    if a > b: return 1
    elif a == b: return 0
    else: return -1

def solve():
    a, b, c, d = map(int, input().split())
    ans = 0
    if f(a, c) + f(b, d) > 0: ans += 1
    if f(a, d) + f(b, c) > 0: ans += 1
    if f(b, c) + f(a, d) > 0: ans += 1
    if f(b, d) + f(a, c) > 0: ans += 1
    print(ans)

def main():
    t = 1
    t = int(inp())  # Uncomment if multiple test cases exist
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()