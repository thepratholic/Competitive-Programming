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

    if n == 1:
        print(a[0])
        return
    ans = sum(a)
    while n > 1:
        n -= 1
        a = a[::-1]
        a = [a[i+1] - a[i] for i in range(n)]
        ans = max(ans, abs(sum(a)))
    print(ans)

def main():
    t = 1
    t = int(inp())  # Uncomment if multiple test cases exist
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()