import sys

def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))


def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    l, r = map(int, input().split())
    L, R = map(int, input().split())

    print( max(1, min(r, R) - max(l, L) + (l != L) + (r != R)) )



def main():
    t = 1
    t = int(inp())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()