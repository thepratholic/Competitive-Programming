def is_good(arr):
    s = 0
    for x in arr:
        s += x
        if s % 3 == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []

    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N

        if is_good(A):
            results.append("Yes")
            continue

        found = False
        for i in range(1, N + 1):
            B = A[:i][::-1] + A[i:]
            if is_good(B):
                found = True
                break
        results.append("Yes" if found else "No")

    print("\n".join(results))