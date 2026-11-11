import sys
input = sys.stdin.readline

def query(a):
    print("? ", a, flush=True)
    return int(input())

def solve():
    n = int(input())

    low, high = 1, n
    ans = 1

    while low <= high:
        mid = (low + high) >> 1

        if mid == 1:
            a = 10**9
        else:
            a = query(mid - 1)

        b = query(mid)

        if mid == n:
            c = 10**9
        else:
            c = query(mid + 1)

        if a > b and c > b:
            ans = mid
            break

        if a > b:
            low = mid + 1
        else:
            high = mid - 1

    print("! ", ans, flush=True)

if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
    solve()
