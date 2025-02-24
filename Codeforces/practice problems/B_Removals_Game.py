import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

def solve():
    n = int(inp())
    a = inplist()
    b = inplist()

    if a == b:
        print("Bob")
        return

    a.reverse()  # Reverse 'a' instead of sorting 'b'
    if a == b:
        print("Bob")
        return

    print("Alice")

def main():
    t = int(inp())  # Read the number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
