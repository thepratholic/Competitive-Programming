from bisect import bisect_left

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prev = float('-inf')
    b.sort()

    for i in range(n):
        idx = bisect_left(b, a[i] + prev)  # Find index of the smallest >= (a[i] + prev)
        
        if idx < m:  # Ensure index is valid
            val = b[idx]  # Get the actual value from `b`

            if a[i] < prev:
                a[i] = val - a[i]
            else:
                a[i] = min(a[i], val - a[i])

        if a[i] < prev:
            print("NO")
            return
        prev = a[i]

    print("YES")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
