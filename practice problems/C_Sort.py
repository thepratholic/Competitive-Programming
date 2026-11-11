import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    prefix_a = [[0] * 26 for _ in range(n + 1)]
    prefix_b = [[0] * 26 for _ in range(n + 1)]

    for i in range(n):
        for j in range(26):
            prefix_a[i + 1][j] = prefix_a[i][j]
            prefix_b[i + 1][j] = prefix_b[i][j]
        prefix_a[i + 1][ord(a[i]) - ord('a')] += 1
        prefix_b[i + 1][ord(b[i]) - ord('a')] += 1

    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())

        changes = 0
        for j in range(26):
            freq_a = prefix_a[r][j] - prefix_a[l - 1][j]
            freq_b = prefix_b[r][j] - prefix_b[l - 1][j]
            changes += abs(freq_a - freq_b)

        print(changes // 2)

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()