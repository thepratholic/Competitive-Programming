import sys
from collections import Counter
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)

    odd_vals = 0
    even_vals = 0

    for v in freq.values():
        if v & 1:
            odd_vals += 1
        else:
            even_vals += 1

    k = min(even_vals, n)

    if ((n - k) & 1) and odd_vals == 0:
        k -= 1
        if k < 0:
            k = 0

    print(odd_vals + 2 * k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
