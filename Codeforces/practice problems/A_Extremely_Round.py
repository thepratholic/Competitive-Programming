def check(x):
    s = str(x)
    if len(s) == 1:
        return True
    for i in range(1, len(s)): 
        if s[i] != '0':
            return False
    return True

MAXN = 10**6 + 10
A = [0] * (MAXN)

def pre():
    for i in range(1, MAXN):
        A[i] = A[i-1] + check(i)

def solve():
    n = int(input())
    print(A[n])

def main():
    pre()
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
