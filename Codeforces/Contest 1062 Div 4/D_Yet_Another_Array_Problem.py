import sys
from math import gcd
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    g = a[0]
    for val in a[1:]:
        g = gcd(g, val)

    for x in range(2, 100):  
        if gcd(g, x) == 1:
            print(x)
            return
    
    print(-1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
