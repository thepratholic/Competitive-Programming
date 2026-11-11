import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, l, r = map(int, input().split())
    
    a = list(map(int, input().split()))
    l -= 1
    r -= 1
    x, y = [], []

    x = a[l:]
    y = a[:r+1]
    
    x.sort()
    y.sort()

    k = r - l + 1
    
    s1 = sum(x[:k])
    s2 = sum(y[:k])
    
    print(min(s1, s2))

def main():
    t = 1
    t = int(inp())  # Uncomment if multiple test cases exist
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()