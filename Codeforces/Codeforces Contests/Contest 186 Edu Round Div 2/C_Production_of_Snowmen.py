import sys

def solve():

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    bb = b + b
    cc = c + c

    c1 = 0
    for s in range(n):
        if all(a[i] < bb[i+s] for i in range(n)):
            c1 += 1

    c2 = 0
    for s in range(n):
        if all(b[i] < cc[i+s] for i in range(n)):
            c2 += 1
            
    print(c1 * c2 * n)

if __name__ == '__main__':

    t = int(input())
    for _ in range(t):
        solve()