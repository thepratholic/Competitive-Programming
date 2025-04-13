import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = [0]*(2*n+1)
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j in range(1, n+1):
            p[i+j] = row[j-1]
    s = set(p[2:])
    missing = next(x for x in range(1, 2*n+1) if x not in s)
    p[1] = missing
    sys.stdout.write(" ".join(str(p[i]) for i in range(1,2*n+1))+"\n")
