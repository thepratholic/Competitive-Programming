def solve():
    # Read parameters for one test case
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    T = sum(a)
    total = k * T

    if total < x:
        print(0)
        return

    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = P[i - 1] + a[i - 1]

    X = total - x
    ans = 0
    for i in range(n):
        if X >= P[i]:
            m_max = (X - P[i]) // T 
            count_i = min(k, m_max + 1)
            ans += count_i
    print(ans)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline 
    t = int(input())  
    for _ in range(t):
        solve()
