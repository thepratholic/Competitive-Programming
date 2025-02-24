import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)


def solve():
    n = int(input())
    s_x, s_y, s_z = 0, 0, 0

    for _ in range(n):
         x, y, z = map(int, input().split())

         s_x += x
         s_y += y
         s_z += z

    if s_x == 0 and s_y == 0 and s_z == 0:
         print("YES")
    else: print("NO")

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()