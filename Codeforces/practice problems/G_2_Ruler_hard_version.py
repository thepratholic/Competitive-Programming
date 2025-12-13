import sys
input = sys.stdin.readline

def query(a, b):
    print(f"? {a} {b}", flush=True)
    return int(input())

def solve():
    low, high = 0, 1000

    while high - low > 1:
        a = (2 * low + high) // 3
        b = (low + 2 * high) // 3

        res = query(a, b)

        if res == a * b:
            low = b
        elif res == a * (b + 1):
            low = a
            high = b
        else:
            high = a

    print(f"! {high}", flush=True)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
