import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    S = input().strip()
    T = input().strip()

    try:
        p = S.index('1')
    except ValueError:
        if '1' in T:
            print(-1)
        else:
            print(0)
        return

    if any(T[i] != '0' for i in range(p)) or T[p] != '1':
        print(-1)
        return

    ops = []
    for j in range(p+1, n):
        if S[j] == '0':
            ops.append(j)    

    for j in range(n-1, p, -1):
        if T[j] == '0':
            ops.append(j)    

    print(len(ops))
    if ops:
        print(*ops)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
