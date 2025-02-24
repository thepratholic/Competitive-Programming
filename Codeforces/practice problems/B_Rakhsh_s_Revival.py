import sys

# Fast Input
def inp(): return sys.stdin.readline().strip()
def inplist(): return list(map(int, inp().split()))

# Debugging function
def debug(*args):
    print("DEBUG:", *args, file=sys.stderr)

def solve():
    n, m, k = map(int, input().split())
    s = input()
    cnt_zeros, min_ops = 0, 0
    i = 0
    while i < n:
        if s[i] == "0":
            cnt_zeros += 1
            if cnt_zeros == m:
                min_ops += 1
                cnt_zeros = 0
                i += k-1
        else:
            cnt_zeros = 0
        i += 1
    print(min_ops)

def main():
    t = 1
    t = int(inp())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()