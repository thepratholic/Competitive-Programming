import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    s  = input().lower()
    vowels = ["a", "e", "i", "o", "u", "y"]

    res = ""

    for i in s:
        if i in vowels:
             continue
        else:
             res += "."
             res += i

    print(res)

def main():
    # t = 1
    # t = int(inp())  # Uncomment if multiple test cases exist
    # for _ in range(t):
        solve()

if __name__ == "__main__":
    main()