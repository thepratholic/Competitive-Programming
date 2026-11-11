import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    s = input()

    i = 0
    should = "hello"

    for t in s:
         if t == should[i]:
              i += 1
         if i == len(should):
              break
    if i == len(should):
         print("YES")
    else:
         print("NO")

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()