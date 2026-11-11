import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, m, q = map(int, input().split())
    b = sorted(list(map(int, input().split())))
    a = list(map(int, input().split()))

    if b[0] < a[0] < b[1]:
        print((b[1] - b[0]) // 2)
    elif a[0] < b[0]:
        print(b[0] - 1)
    else:
        print(n - b[1])

def main():
    t = 1
    t = int(inp())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()