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
    

    for i in range(n-1):
        if a[i] > a[i+1]:
            print("NO")
            return
        else:
            tmp = min(a[i], a[i + 1])
            a[i] -= tmp
            a[i+1] -= tmp

    print("YES")

def main():
    t = 1
    t = int(inp())  # Uncomment if multiple test cases exist
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()